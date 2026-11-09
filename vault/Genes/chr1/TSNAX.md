---
symbol: "TSNAX"
type: "gene"
col: 3856
ensembl_id: "ENSG00000116918"
name: "translin associated factor X"
location: "1q42.2"
module: 65
arm: "+"
pooled_cpm: 65.78
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# TSNAX

*translin associated factor X* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.79× (z +12.7, q 3e-34, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.471×, AsPC-1 0.502×, PANC-1 0.634×, A498 0.612×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.391×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACP1]] (+0.67, fdr 7e-06), [[UBA5]] (+0.63, fdr 1e-05), [[MTX2]] (+0.62, fdr 1e-05); moves opposite to [[GATAD2A]] (-0.61, fdr 7e-06), [[PKNOX1]] (-0.61, fdr 1e-05), [[STAG1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3856.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +12.7 | 3e-34 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +12.3 | 1e-32 | 44/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +11.0 | 1e-25 | 44/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +10.8 | 5e-25 | 33/48 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.53×** | +9.2 | 3e-18 | 33/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +8.3 | 1e-14 | 28/48 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +7.1 | 1e-10 | 27/48 (CFPAC-1, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +6.9 | 3e-10 | 32/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.24×** | +6.5 | 4e-09 | 23/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +6.1 | 4e-08 | 26/48 (SW480, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +5.0 | 3e-05 | 31/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +4.6 | 2e-04 | 23/50 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.22×** | +4.1 | 0.001 | 18/43 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 15/48 (C32, A-427, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.003 | 19/48 (NCI-H2030, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.008 | 20/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.4 | 0.020 | 10/48 (SK-MEL-2, COLO 205, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.10× | +3.0 | 0.066 | 7/48 (SW48, RKO, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.078 | 12/47 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.078 | 14/48 (NCI-H460, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3856.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.471×, AsPC-1 0.502×, PANC-1 0.634×, A498 0.612×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.391×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.846× | -3.7 | 0.14 | 21/47 (hTERT-HPNE, SW480, …) | two highest doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.4 | 0.17 | 20/48 (SW1417, NCI-H460, …) | two highest doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.906× | -3.1 | 0.34 | 9/48 (NCI-H661, NCI-H1573, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.908× | -3.0 | 0.34 | 3/48 (MIA PaCa-2, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3856. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 77.0 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +26.5) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.10× (z +18.7) | — |
| [[HEC-1-A (line)]] | alt | 47.6 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 81.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.14× (z +11.0) | — |
| [[SW480 (line)]] | alt | 51.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 67.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[SK-MEL-2 (line)]] | alt | 91.2 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.80× (z +17.2) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.68× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 55.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.70× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 60.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 57.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +10.3) | — |
| [[RKO (line)]] | wt | 58.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.69× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[A-427 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -15.3) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A498 (line)]] | wt | 96.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.612× (z -8.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 45.6 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.73× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 64.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[hTERT-HPNE (line)]] | wt | 60.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.9) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[J82 (line)]] | alt | 55.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.1) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[LS 180 (line)]] | wt | 68.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.17× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 70.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.634× (z -9.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SNU-423 (line)]] | alt | 47.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +14.1) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[AN3 CA (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 95.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 88.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3856), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACP1]] | +0.67 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[UBA5]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[MTX2]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NDUFV2]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ATG4C]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[VAMP4]] | +0.60 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[ANAPC4]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[COX15]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MRS2]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PIKFYVE]] | +0.58 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[TGDS]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.61 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[PKNOX1]] | -0.61 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[STAG1]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[PPRC1]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[RASAL2]] | -0.51 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[MFSD14CP-1]] | -0.50 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[ARHGAP39]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[INO80]] | -0.50 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[NUTM2A-AS1]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[KPNA4]] | -0.49 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SPON1-AS1]] | -0.49 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[CDR2]] | -0.48 | -0.40 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.3, -10.4); signed map (-30.4, -14.2). **Vector** length 98.0, 24.6% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.4 | +7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[NG25 (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +2.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.8 | +6.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -2.4 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | translin associated factor X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:231,528,541-231,566,524 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRAX, C3PO |
| Gene groups (HGNC) | Endoribonucleases |
| Reactome | 2 pathways, smallest: Small interfering RNA (siRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99598](https://www.uniprot.org/uniprotkb/Q99598) (RNA endonuclease TRAX):

> As part of the Translin-TRAX complex, exhibits single-stranded endoribonuclease activity. The Translin-TRAX complex participates in the activation of the RNA-induced silencing complex (RISC) by degrading siRNA passenger strand cleavage products. Possible role in spermatogenesis. May play a role in tRNA processing by degrading 5' pre-tRNA fragments (By similarity).; Facilitates the activation of checkpoint kinase ATM during DNA damage checkpoint signaling, a function it may perform independently …

**Summary**, from NCBI Gene [7257](https://www.ncbi.nlm.nih.gov/gene/7257):

> This gene encodes a protein which specifically interacts with translin, a DNA-binding protein that binds consensus sequences at breakpoint junctions of chromosomal translocations. The encoded protein contains bipartite nuclear targeting sequences that may provide nuclear transport for translin, which lacks any nuclear targeting motifs. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12380) · Entrez [7257](https://www.ncbi.nlm.nih.gov/gene/7257) · UniProt [Q99598](https://www.uniprot.org/uniprotkb/Q99598) · Ensembl [ENSG00000116918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116918)

## Data

Gene col 3856: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3856); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3856, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3856]; `tensor/DDL_lfc|DDL_z.npy` [3856]; `embed/gene_vectors.npy` [3856]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3856 or target_col == 3856). Every well: [[TSNAX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSNAX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
