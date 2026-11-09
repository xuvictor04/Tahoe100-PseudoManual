---
symbol: "RRP1B"
type: "gene"
col: 8318
ensembl_id: "ENSG00000160208"
name: "ribosomal RNA processing 1B"
location: "21q22.3"
module: 33
arm: "+"
pooled_cpm: 60.42
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RRP1B

*ribosomal RNA processing 1B* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.41× (z +15.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.559× (z -14.6, q 3e-45, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKS6]] (+0.77, fdr 7e-06), [[NLE1]] (+0.74, fdr 7e-06), [[DKC1]] (+0.72, fdr 7e-06); moves opposite to [[USP34-DT]] (-0.68, fdr 3e-05), [[UPK2]] (-0.68, fdr 3e-05), [[KDM6A]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +15.5 | 0e+00 | 47/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.28×** | +14.6 | 1e-45 | 47/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.23×** | +14.2 | 3e-43 | 46/48 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +10.4 | 2e-23 | 45/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +8.3 | 2e-14 | 43/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +7.1 | 1e-10 | 34/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +6.1 | 8e-08 | 30/48 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.40×** | +5.7 | 1e-06 | 31/47 (C32, SNU-423, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.83×** | +5.6 | 1e-06 | 37/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +5.3 | 6e-06 | 29/47 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.35×** | +5.2 | 8e-06 | 21/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.76×** | +5.2 | 8e-06 | 32/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.36×** | +5.2 | 8e-06 | 29/47 (NCI-H1792, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.33×** | +5.1 | 1e-05 | 27/47 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.0 | 3e-05 | 27/48 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.67×** | +4.7 | 8e-05 | 27/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +4.7 | 8e-05 | 26/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.7 | 1e-04 | 30/48 (A-172, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +4.5 | 2e-04 | 29/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.017 | 17/48 (MIA PaCa-2, H4, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.020 | 19/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.031 | 15/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.050 | 11/48 (C32, NCI-H2347, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.052 | 14/48 (A498, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.559×** | -14.6 | 3e-45 | 40/48 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -6.4 | 5e-08 | 30/48 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.4 | 0.002 | 20/48 (SK-MEL-2, A-427, …) | top dose only | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.017 | 20/49 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rifaximin (drug)]] 5 µM |  | 0.826× | -3.3 | 0.13 | 19/48 (C-33 A, AN3 CA, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.884× | -3.1 | 0.18 | 19/48 (HOP62, SW1417, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.836× | -3.1 | 0.18 | 15/47 (Hs 766T, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 92.9 | 4 (2 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.64× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.9) |
| [[A-172 (line)]] | wt | 75.5 | 3 (2 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.86× (z +10.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.41× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 47.4 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.98× (z +11.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.87× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 61.4 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 38.4 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.04× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.53× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 35.3 | 4 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.40× (z +11.0) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.32× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 46.6 | 4 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.23× (z +11.3) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.74× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 56.0 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.94× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.75× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 39.5 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +11.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.28× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 31.1 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 5.08× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.91× (z +9.8) | — |
| [[H4 (line)]] | wt | 45.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.25× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 40.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.89× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 109 | 2 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.60× (z +10.5) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.49× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -17.5) |
| [[RKO (line)]] | wt | 110 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -20.0) |
| [[SNU-423 (line)]] | alt | 31.8 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.28× (z +8.7) | — |
| [[A549 (line)]] | wt | 42.1 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.78× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 41.6 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.12× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -10.4) |
| [[HT-29 (line)]] | alt | 29.4 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.16× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 31.9 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.67× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 71.9 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.43× (z +8.5) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 51.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 115 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -11.7) |
| [[A-427 (line)]] | wt | 80.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.16× (z +10.5) ⚠ unreliable plate only | — |
| [[AN3 CA (line)]] | alt | 81.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.188× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[C-33 A (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 80.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -10.5) |
| [[Hs 766T (line)]] | wt | 41.9 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.03× (z +8.5) ⚠ unreliable plate only | — |
| [[LoVo (line)]] | wt | 80.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -20.4) |
| [[SNU-1 (line)]] | wt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -13.6) |
| [[SW1417 (line)]] | alt | 69.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -15.7) |
| [[BT-474 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKS6]] | +0.77 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[NLE1]] | +0.74 | +0.65 / +0.72 | both halves | 7e-06 | STRING 799 |
| [[DKC1]] | +0.72 | +0.75 / +0.72 | both halves | 7e-06 | STRING 535 |
| [[POLRMT]] | +0.71 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[TMEM177]] | +0.71 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.70 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[NKRF]] | +0.69 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[FXN]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.68 | +0.72 / +0.63 | both halves | 7e-06 | same gene group |
| [[CHCHD6]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 | same gene group |
| [[MRPL4]] | +0.67 | +0.60 / +0.56 | both halves | 1e-05 | STRING 543 |
| [[POLR3H]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP34-DT]] | -0.68 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[UPK2]] | -0.68 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[KDM6A]] | -0.67 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[KMT2E-AS1]] | -0.66 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[AP4S1]] | -0.66 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ZNF451-AS1]] | -0.66 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[MALINC1]] | -0.65 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | -0.65 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[ZNF490]] | -0.65 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[C11orf71]] | -0.64 | -0.57 / -0.29 | both halves | 3e-04 |  |
| [[PBLD]] | -0.64 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[EFCAB5]] | -0.64 | -0.52 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RRP1B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SACS]] | B | SACS activity raises RRP1B's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without SACS | 0.012 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[GARNL3]] | C | GARNL3 activity raises RRP1B's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without GARNL3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[S100A13]] | C | S100A13 activity lowers RRP1B's level | lines that do not express S100A13 (4) vs lines expressing it (46) | 1.55× higher at baseline in the lines without S100A13 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CASP4, SP100, KIFC3; maybe low, not absent; its own permutation p |
| [[TXNL4A]] | C | TXNL4A's natural level weakens RRP1B's drug response | TXNL4A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.01; direction not clear | 0.090 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.0, -40.7); signed map (-9.5, -53.1). **Vector** length 119, 36.9% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.50 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.51 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.6 | +10.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +7.5 | +14.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.5 | +15.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +7.2 | +14.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +8.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.5 | +5.6 |
|  | [[EX229 (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +7.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.6 | -14.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal RNA processing 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:43,659,560-43,696,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Nnp1, RRP1, PPP1R136; previously KIAA0179 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14684](https://www.uniprot.org/uniprotkb/Q14684) (Ribosomal RNA processing protein 1 homolog B):

> Positively regulates DNA damage-induced apoptosis by acting as a transcriptional coactivator of pro-apoptotic target genes of the transcriptional activator E2F1. Likely to play a role in ribosome biogenesis by targeting serine/threonine protein phosphatase PP1 to the nucleolus. Involved in regulation of mRNA splicing (By similarity). Inhibits SIPA1 GTPase activity (By similarity). Involved in regulating expression of extracellular matrix genes (By similarity). Associates with chromatin and may …

**Summary**, from NCBI Gene [23076](https://www.ncbi.nlm.nih.gov/gene/23076):

> Enables transcription coactivator activity. Involved in cellular response to virus; positive regulation of apoptotic process; and positive regulation of transcription by RNA polymerase II. Located in chromosome; granular component; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23818) · Entrez [23076](https://www.ncbi.nlm.nih.gov/gene/23076) · UniProt [Q14684](https://www.uniprot.org/uniprotkb/Q14684) · Ensembl [ENSG00000160208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160208)

## Data

Gene col 8318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8318); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8318]; `tensor/DDL_lfc|DDL_z.npy` [8318]; `embed/gene_vectors.npy` [8318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8318 or target_col == 8318). Every well: [[RRP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
