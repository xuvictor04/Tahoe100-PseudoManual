---
symbol: "POGLUT3"
type: "gene"
col: 10907
ensembl_id: "ENSG00000178202"
name: "protein O-glucosyltransferase 3"
location: "11q22.3"
module: 43
arm: "-"
pooled_cpm: 21.19
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 33
n_dd_up_clean: 4
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/043", "written"]
generated_by: "tahoemap"
---

# POGLUT3

*protein O-glucosyltransferase 3* — 11q22.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> POGLUT3, formerly KDELC2, is an ER protein O-glucosyltransferase that modifies a specific serine in correctly folded EGF repeats of Notch receptors and some matrix proteins.

## What it is

Despite its KDEL motif this is a glucosyltransferase, not part of KDEL-receptor retrieval. With its paralogue POGLUT2 (KDELC1) it adds glucose to a serine between the third and fourth conserved cysteines of an EGF repeat, a position distinct from the sites POGLUT1 uses. Only properly folded repeats are accepted. Losing the site, together with nearby O-fucose sites, reduces NOTCH1 surface presentation and ligand responsiveness, so the modification reads as a folding and trafficking checkpoint rather than a signalling switch. Later work extended the substrates beyond Notch to fibrillins and LTBP1. Past that the record is thin: no human disease is firmly attributed to it, and nothing is established about its transcriptional regulation.

## What is uncertain

Its membership of the p53 programme in the earlier MG53/p53 study was the weak kind, holding in only some cross-fitting folds, so it may be a borderline gene that cleared a threshold rather than a real part of the response. No mechanism connects a Notch glycosyltransferase to p53, and with nothing known about its promoter there is no indirect route to check either; the transcriptional slowdown of arresting cells would give the same direction.

## References

- Takeuchi et al., 2018, PNAS — identified KDELC1 and KDELC2 as protein O-glucosyltransferases POGLUT2 and POGLUT3, modifying an EGF-repeat site distinct from POGLUT1's.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.07× (z +19.8, q 0e+00, up in 35 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.33× (z +3.5, q 0.026, up in 19 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.279× (z -15.5, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBX5]] (+0.72, fdr 7e-06), [[TYMS]] (+0.72, fdr 7e-06), [[FOXM1]] (+0.71, fdr 7e-06); moves opposite to [[RPL23]] (-0.70, fdr 7e-06), [[RPL18]] (-0.70, fdr 7e-06, ⚠ RPL18 in the vector space only through flagged drug-doses), [[NACA4P]] (-0.69, fdr 7e-06, ⚠ NACA4P in the vector space only through flagged drug-doses), [[RPL31]] (-0.67, fdr 1e-05), [[RPL36]] (-0.67, fdr 7e-06).
> It sits in the **-** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); 10 go from it, the strongest it → [[MANEA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **5.07×** | +19.8 | 0e+00 | 35/36 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.16×** | +16.7 | 0e+00 | 30/30 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.26×** | +13.3 | 3e-38 | 29/32 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.32×** | +4.8 | 2e-04 | 24/43 (NCI-H2347, SW480, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.41×** | +4.2 | 0.003 | 20/43 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.41×** | +4.1 | 0.005 | 18/39 (Hs 766T, C32, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.23×** | +3.6 | 0.023 | 11/43 (LOX-IMVI, COLO 205, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.34×** | +3.6 | 0.023 | 15/43 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.026 | 19/43 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.089 | 9/43 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.089 | 9/43 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.089 | 12/43 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.28× | +3.0 | 0.10 | 14/43 (PANC-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.279×** | -15.5 | 0e+00 | 42/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.338×** | -13.1 | 6e-37 | 39/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.356×** | -12.5 | 1e-33 | 38/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.579×** | -9.3 | 2e-18 | 24/42 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.467×** | -9.2 | 4e-18 | 36/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.483×** | -8.8 | 1e-16 | 38/42 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.518×** | -6.7 | 2e-09 | 31/42 (LOX-IMVI, A-172, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.625×** | -5.7 | 1e-06 | 27/43 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.415×** | -5.6 | 2e-06 | 26/43 (MIA PaCa-2, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.637×** | -5.4 | 3e-06 | 23/43 (C-33 A, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.741×** | -5.1 | 2e-05 | 22/43 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.786×** | -4.1 | 0.002 | 17/43 (HCT15, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.716×** | -4.0 | 0.002 | 20/41 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.730×** | -3.8 | 0.006 | 19/43 (CHP-212, H4, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.689×** | -3.8 | 0.006 | 19/43 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.740×** | -3.6 | 0.010 | 18/42 (SW 900, SW480, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.749×** | -3.5 | 0.016 | 19/42 (HOP62, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.018 | 19/42 (MIA PaCa-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.6 | 3 (3 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.68× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Belinostat (drug)]] 5 µM 0.0795× (z -24.6) |
| [[HOP62 (line)]] | alt | 29.0 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -13.9) |
| [[C32 (line)]] | wt | 22.6 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 5 µM 0.134× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 21.8 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 8.10× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Belinostat (drug)]] 0.5 µM 0.239× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 22.8 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 26.0 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.3) |
| [[Hs 766T (line)]] | wt | 24.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.9) |
| [[HS-578T (line)]] | alt | 20.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.83× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -8.9) |
| [[LoVo (line)]] | wt | 19.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 5.48× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Belinostat (drug)]] 5 µM 0.116× (z -12.3) |
| [[A-172 (line)]] | wt | 34.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Belinostat (drug)]] 5 µM 0.201× (z -11.5) |
| [[A498 (line)]] | wt | 23.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.0) |
| [[C-33 A (line)]] | alt | 49.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -12.4) |
| [[H4 (line)]] | wt | 62.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -11.2) |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.111× (z -11.0) |
| [[J82 (line)]] | alt | 17.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 41.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 30.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 32.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -10.6) |
| [[HT-29 (line)]] | alt | 9.70 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.29× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 14.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.23× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SNU-423 (line)]] | alt | 14.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.32× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 13.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.35× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0957× (z -8.5) |
| [[BT-474 (line)]] | alt | 7.58 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0865× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 57.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H661 (line)]] | alt | 65.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 5.57 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0667× (z -9.9) |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -9.0) |
| [[SW 900 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX5]] | +0.72 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[TYMS]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[FOXM1]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[CENPH]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[HELLS]] | +0.70 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[PIGK]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[TMPO]] | +0.68 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[TIMELESS]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[FAM111A]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[FH]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[KNTC1]] | +0.65 | +0.58 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 15 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL23]] | -0.70 | -0.60 / -0.71 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | -0.70 | -0.66 / -0.67 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA4P]] ⚠ | -0.69 | -0.65 / -0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL37]] ⚠ | -0.68 | -0.65 / -0.67 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | -0.67 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[RPL36]] | -0.67 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[RPS27]] | -0.67 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[RPL26]] | -0.66 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.66 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[RPS13]] ⚠ | -0.66 | -0.56 / -0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | -0.66 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.66 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[SNHG6]] | -0.66 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[EPB41L4A-AS1]] | -0.66 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[RPS10]] | -0.66 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.65 | -0.49 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises POGLUT3's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.90× lower at baseline in the lines without MYBL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[PTGFRN]] | B | PTGFRN activity lowers POGLUT3's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.91× higher at baseline in the lines without PTGFRN | 0.071 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[SCARA3]] | B | SCARA3 activity raises POGLUT3's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without SCARA3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[OXCT1]] | B | OXCT1 activity raises POGLUT3's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without OXCT1 | 0.074 | ⚠ within organs, on part of the lines |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANEA]] | B | POGLUT3 activity raises MANEA's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without POGLUT3 | 0.028 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[ZWINT]] | B | POGLUT3 activity raises ZWINT's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.50× lower at baseline in the lines without POGLUT3 | 0.047 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[LMBRD2]] | B | POGLUT3 activity raises LMBRD2's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without POGLUT3 | 0.048 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[BACE1]] | B | POGLUT3 activity raises BACE1's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without POGLUT3 | 0.055 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[PIGT]] | B | POGLUT3 activity raises PIGT's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without POGLUT3 | 0.060 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[HMGN2]] | B | POGLUT3 activity raises HMGN2's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without POGLUT3 | 0.060 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[MYBL1]] | B | POGLUT3 activity raises MYBL1's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 2.31× lower at baseline in the lines without POGLUT3 | 0.062 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[CBX5]] | B | POGLUT3 activity raises CBX5's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.24× lower at baseline in the lines without POGLUT3 | 0.087 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[MCM3]] | B | POGLUT3 activity raises MCM3's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without POGLUT3 | 0.097 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[MCM4]] | B | POGLUT3 activity raises MCM4's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without POGLUT3 | 0.099 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **-** arm (projection on the module's main direction -0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-41.9, -27.6); signed map (-33.3, -47.5). **Vector** length 104, 27.9% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +9.0 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +8.3 | +19.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.3 | +1.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.8 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -8.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.0 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -5.4 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.4 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -1.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | protein O-glucosyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:108,472,112-108,498,405 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33424; previously KDELC2 |
| Gene groups (HGNC) | Glycosyltransferase family 90 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4H8](https://www.uniprot.org/uniprotkb/Q7Z4H8) (Protein O-glucosyltransferase 3):

> Protein glucosyltransferase that catalyzes the transfer of glucose from UDP-glucose to a serine residue within the consensus sequence peptide C-X-N-T-X-G-S-F-X-C. Can also catalyze the transfer of xylose from UDP-xylose but less efficiently. Specifically targets extracellular EGF repeats of proteins such as NOTCH1, NOTCH3, FBN1, FBN2 and LTBP1. May regulate the transport of NOTCH1 and NOTCH3 to the plasma membrane and thereby the Notch signaling pathway.

**Summary**, from NCBI Gene [143888](https://www.ncbi.nlm.nih.gov/gene/143888):

> Enables UDP-glucosyltransferase activity and UDP-xylosyltransferase activity. Involved in protein O-linked glycosylation via glucose. Predicted to be located in endoplasmic reticulum lumen. Predicted to be active in endomembrane system. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28496) · Entrez [143888](https://www.ncbi.nlm.nih.gov/gene/143888) · UniProt [Q7Z4H8](https://www.uniprot.org/uniprotkb/Q7Z4H8) · Ensembl [ENSG00000178202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178202)

## Data

Gene col 10907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10907); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10907]; `tensor/DDL_lfc|DDL_z.npy` [10907]; `embed/gene_vectors.npy` [10907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10907 or target_col == 10907). Every well: [[POGLUT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/POGLUT3.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
