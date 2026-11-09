---
symbol: "EGLN3"
type: "gene"
col: 4984
ensembl_id: "ENSG00000129521"
name: "egl-9 family hypoxia inducible factor 3"
location: "14q13.1"
module: 99
arm: "+"
pooled_cpm: 149.92
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# EGLN3

*egl-9 family hypoxia inducible factor 3* — 14q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +14.6, q 1e-45, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.569× (z -13.2, q 9e-37, down in 40 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.595× (z -12.1, q 3e-31, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A3]] (+0.59, fdr 1e-05), [[C4orf3]] (+0.54, fdr 3e-05), [[POR]] (+0.54, fdr 4e-05); moves opposite to [[CTPS2]] (-0.49, fdr 2e-04), [[USP24]] (-0.47, fdr 6e-05), [[STRIP1]] (-0.45, fdr 4e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SLC6A14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +14.6 | 1e-45 | 45/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +11.0 | 1e-25 | 43/49 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +8.4 | 1e-14 | 30/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +7.3 | 3e-11 | 29/48 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +7.2 | 7e-11 | 24/48 (Panc 03.27, SK-MEL-2, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.67×** | +6.5 | 8e-09 | 33/48 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +6.4 | 1e-08 | 32/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +5.5 | 4e-06 | 25/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.18× | +4.1 | 0.003 | 20/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.17× | +3.9 | 0.006 | 14/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.007 | 16/47 (RKO, NCI-H2347, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.010 | 13/48 (A-427, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.15× | +3.4 | 0.028 | 13/48 (Panc 03.27, LoVo, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.049 | 15/47 (HOP62, C32, …) | two highest doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.086 | 16/47 (A549, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -13.2 | 9e-37 | 40/47 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.595×** | -12.1 | 3e-31 | 37/48 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -10.5 | 2e-23 | 32/42 (A-427, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.701×** | -8.6 | 1e-15 | 28/49 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.718×** | -8.0 | 1e-13 | 28/48 (COLO 205, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.733×** | -7.5 | 4e-12 | 30/48 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -6.4 | 2e-08 | 29/48 (LS 180, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.775×** | -6.2 | 4e-08 | 27/48 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.768×** | -6.2 | 5e-08 | 28/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.780×** | -6.0 | 9e-08 | 29/48 (KATO III, LS 180, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.856× | -5.3 | 5e-06 | 22/49 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -5.3 | 6e-06 | 24/48 (C32, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.814×** | -4.8 | 7e-05 | 23/50 (C32, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.824×** | -4.7 | 1e-04 | 23/48 (HepG2/C3A, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.824×** | -4.7 | 1e-04 | 22/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.883× | -4.3 | 7e-04 | 16/48 (AsPC-1, C32, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.841× | -4.2 | 9e-04 | 20/48 (A-427, RPMI-7951, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.726×** | -4.1 | 0.001 | 17/46 (H4, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.730×** | -4.0 | 0.002 | 23/49 (C32, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.798×** | -3.9 | 0.002 | 16/47 (SNU-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 890 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0932× (z -27.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.273× (z -14.8) |
| [[KATO III (line)]] | alt | 308 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.276× (z -13.2) |
| [[LS 180 (line)]] | wt | 250 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.366× (z -11.6) |
| [[SW480 (line)]] | alt | 140 | 5 (3 ⚠) | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.60× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.522× (z -9.4) |
| [[BT-474 (line)]] | alt | 284 | 2 | 6 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.37× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 333 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.190× (z -14.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.266× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 444 | 0 | 8 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.264× (z -14.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.273× (z -13.7) |
| [[Hs 766T (line)]] | wt | 219 | 1 | 6 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.76× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.300× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 111 | 6 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.01× (z +10.4) | [[Harringtonine (drug)]] 5 µM 0.497× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 186 | 1 | 5 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.23× (z +11.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.232× (z -14.2) ⚠ toxic |
| [[A549 (line)]] | wt | 151 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.96× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.282× (z -11.9) |
| [[HT-29 (line)]] | alt | 173 | 2 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.87× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.302× (z -12.4) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 348 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 299 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.78× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 169 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.68× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -11.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 150 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0720× (z -23.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 171 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.309× (z -9.6) |
| [[LoVo (line)]] | wt | 116 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.64× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.423× (z -11.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 61.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 61.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.10× (z +10.6) | — |
| [[A498 (line)]] | wt | 172 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.57× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 200 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 59.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.40× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -18.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.334× (z -9.7) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -9.3) |
| [[A-172 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 71.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.10× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 117 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.26× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 72.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.90× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 95.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.45× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 128 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 85.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.02× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 86.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.75× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 86.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.96× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 94.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.14× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 117 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.10× (z +12.3) | — |
| [[SW48 (line)]] | wt | 89.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.337× (z -9.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A3]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[C4orf3]] | +0.54 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[POR]] | +0.54 | +0.43 / +0.62 | both halves | 4e-05 |  |
| [[KCNQ1OT1]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[P4HA1]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 698 |
| [[MYO1E]] | +0.51 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[EIF4A3]] | +0.50 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[TNFRSF10D]] | +0.50 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[GBE1]] | +0.50 | +0.49 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[RAB20]] | +0.50 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[PFKFB3]] | +0.49 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[SPTSSA]] | +0.49 | +0.41 / +0.50 | both halves | 4e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[EPAS1]] | +0.49 | +0.45 / +0.50 | both halves | 3e-05 | pathway: Cellular response to hypoxia; STRING 999 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS2]] | -0.49 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[USP24]] | -0.47 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[STRIP1]] | -0.45 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MCCC2]] | -0.45 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[CCDC66]] | -0.45 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[SGPL1]] | -0.45 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[FAIM]] | -0.45 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[ANGEL2]] | -0.44 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[U2SURP]] | -0.43 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[ZNF391]] | -0.43 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[ZNF236]] | -0.42 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[CPLANE1]] | -0.42 | -0.37 / -0.43 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC6A14]] | B | SLC6A14 activity raises EGLN3's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 1.99× lower at baseline in the lines without SLC6A14 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[IGFBP2]] | B | IGFBP2 activity strengthens EGLN3's drug response | lines that do not express IGFBP2 (16) vs lines expressing it (33) | the lines without IGFBP2 respond 0.90× as strongly (z diff +1.18); strongest at Harringtonine 5 µM: 0.85x vs 0.49x (z diff +5.7) | 0.045 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4; target measured in part of the lines; artifact flags |
| [[DIRC3]] | B | DIRC3 activity raises EGLN3's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without DIRC3 | 0.052 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[RAB20]] | B | RAB20 activity raises EGLN3's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without RAB20 | 0.067 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EGLN3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers EGLN3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GABRA2]] | B | GABRA2 activity raises EGLN3's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 1.52× lower at baseline in the lines without GABRA2 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.1, -16.5); signed map (-36.7, 31.6). **Vector** length 124, 36.2% of its response variance represented; |z| ≥ 3 in 1,508 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.3 | +14.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.2 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.1 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +6.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.8 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +1.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -13.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -4.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.8 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | egl-9 family hypoxia inducible factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.1 — chr14:33,924,227-34,462,774 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PHD3, HIFPH3 |
| Gene groups (HGNC) | Egl-9 family hypoxia inducible factors |
| Hallmark sets | GLYCOLYSIS, MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha; Cellular response to hypoxia; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6Z9](https://www.uniprot.org/uniprotkb/Q9H6Z9) (Prolyl hydroxylase EGLN3):

> Prolyl hydroxylase that mediates hydroxylation of proline residues in target proteins, such as PKM, TELO2, ATF4, GPX4 and HIF1A. Target proteins are preferentially recognized via a LXXLAP motif. Cellular oxygen sensor that catalyzes, under normoxic conditions, the post-translational formation of 4-hydroxyproline in hypoxia-inducible factor (HIF) alpha proteins. Hydroxylates a specific proline found in each of the oxygen-dependent degradation (ODD) domains (N-terminal, NODD, and C-terminal, …

**Summary**, from NCBI Gene [112399](https://www.ncbi.nlm.nih.gov/gene/112399):

> Enables peptidyl-proline 4-dioxygenase activity. Involved in negative regulation of ferroptosis; protein hydroxylation; and protein stabilization. Located in cytosol and nucleus. Implicated in renal cell carcinoma. Biomarker of clear cell renal cell carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14661) · Entrez [112399](https://www.ncbi.nlm.nih.gov/gene/112399) · UniProt [Q9H6Z9](https://www.uniprot.org/uniprotkb/Q9H6Z9) · Ensembl [ENSG00000129521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129521)

## Data

Gene col 4984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4984); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4984]; `tensor/DDL_lfc|DDL_z.npy` [4984]; `embed/gene_vectors.npy` [4984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4984 or target_col == 4984). Every well: [[EGLN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EGLN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
