---
symbol: "DCP2"
type: "gene"
col: 10297
ensembl_id: "ENSG00000172795"
name: "decapping mRNA 2"
location: "5q22.2"
module: 22
arm: "+"
pooled_cpm: 97.93
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# DCP2

*decapping mRNA 2* — 5q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.12× (z +8.0, q 1e-12, up in 0 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.42× (z +7.1, q 3e-10, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.735× (z -6.0, q 1e-06, down in 29 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Sapanisertib (drug)]] 0.5 µM: 0.745× (z -4.2, q 0.003, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIS18BP1]] (+0.61, fdr 1e-05), [[CCDC28A]] (+0.57, fdr 1e-05), [[ARHGAP19]] (+0.57, fdr 1e-05); moves opposite to [[GTPBP4]] (-0.55, fdr 1e-05), [[ASMTL-AS1]] (-0.53, fdr 3e-05), [[PPAN]] (-0.50, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +8.0 | 1e-12 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +7.1 | 3e-10 | 37/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.4 | 4e-08 | 33/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.24×** | +6.1 | 2e-07 | 23/48 (A549, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 3e-06 | 31/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +4.8 | 1e-04 | 26/48 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +4.7 | 2e-04 | 24/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 4e-04 | 27/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.25×** | +4.4 | 6e-04 | 26/48 (A-172, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +4.1 | 0.002 | 21/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.0 | 0.003 | 23/45 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.20×** | +3.7 | 0.011 | 22/48 (RKO, C-33 A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.6 | 0.015 | 22/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.032 | 13/48 (LoVo, SK-MEL-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.18× | +3.3 | 0.034 | 15/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10297.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.735×** | -6.0 | 1e-06 | 29/44 (SK-MEL-2, A-427, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.743×** | -5.8 | 2e-06 | 30/47 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.757×** | -5.6 | 3e-06 | 30/49 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.748×** | -5.5 | 7e-06 | 29/45 (NCI-H2347, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.803×** | -4.5 | 9e-04 | 25/48 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.745×** | -4.2 | 0.003 | 27/48 (SNU-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.007 | 24/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.691×** | -3.9 | 0.007 | 24/48 (NCI-H2347, H4, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.714×** | -3.6 | 0.022 | 23/48 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.890× | -3.4 | 0.042 | 7/48 (CFPAC-1, C-33 A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.857× | -3.2 | 0.084 | 14/48 (A549, HOP62, …) | all doses, flat | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.747×** | -3.1 | 0.094 | 21/48 (HepG2/C3A, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.862× | -3.0 | 0.11 | 5/48 (KATO III, HEC-1-A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 109 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.555× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 134 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 107 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.4) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[HCT15 (line)]] | alt | 100 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.236× (z -10.0) |
| [[RKO (line)]] | wt | 79.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.4) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A-427 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -15.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 84.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[AN3 CA (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 92.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[C32 (line)]] | wt | 63.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.6) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[COLO 205 (line)]] | alt | 99.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 84.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 82.4 | 1 | 0 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 4.57× (z +11.1) | — |
| [[NCI-H661 (line)]] | alt | 88.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0851× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -17.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 92.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 95.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 109 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 84.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 94.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS18BP1]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CCDC28A]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ARHGAP19]] | +0.57 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[NEK2]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[HSD17B11]] | +0.55 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[BORA]] | +0.54 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[BUB3]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CKAP2]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[NUF2]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PRR11]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PTTG1]] | +0.53 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TTK]] | +0.52 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTPBP4]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ASMTL-AS1]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PPAN]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TUBA8]] | -0.48 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[AGAP6]] | -0.47 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[LANCL2]] | -0.47 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[DNAJB12]] | -0.47 | -0.55 / -0.27 | both halves | 3e-04 |  |
| [[TPGS1]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ADCK1]] | -0.45 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[SRRM2-AS1]] | -0.44 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[PVT1]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[INO80]] | -0.44 | -0.51 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.9, -56.9); signed map (-49.8, -39.3). **Vector** length 99.3, 26.0% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +3.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.7 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.4 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Lopinavir (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +2.0 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.2 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | -3.8 | -5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | decapping mRNA 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.2 — chr5:112,976,702-113,022,195 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NUDT20 |
| Gene groups (HGNC) | Nudix hydrolase family; RNA decapping and exonuclease complex subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 12 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IU60](https://www.uniprot.org/uniprotkb/Q8IU60) (m7GpppN-mRNA hydrolase):

> Decapping metalloenzyme that catalyzes the cleavage of the cap structure on mRNAs. Removes the 7-methyl guanine cap structure from mRNA molecules, yielding a 5'-phosphorylated mRNA fragment and 7m-GDP. Necessary for the degradation of mRNAs, both in normal mRNA turnover and in nonsense-mediated mRNA decay. Plays a role in replication-dependent histone mRNA degradation. Has higher activity towards mRNAs that lack a poly(A) tail. Has no activity towards a cap structure lacking an RNA moiety. The …

**Summary**, from NCBI Gene [167227](https://www.ncbi.nlm.nih.gov/gene/167227):

> The protein encoded by this gene is a key component of an mRNA-decapping complex required for degradation of mRNAs, both in normal mRNA turnover, and in nonsense-mediated mRNA decay (NMD). It removes the 7-methyl guanine cap structure from mRNA, prior to its degradation from the 5' end. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:24452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24452) · Entrez [167227](https://www.ncbi.nlm.nih.gov/gene/167227) · UniProt [Q8IU60](https://www.uniprot.org/uniprotkb/Q8IU60) · Ensembl [ENSG00000172795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172795)

## Data

Gene col 10297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10297); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10297]; `tensor/DDL_lfc|DDL_z.npy` [10297]; `embed/gene_vectors.npy` [10297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10297 or target_col == 10297). Every well: [[DCP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
