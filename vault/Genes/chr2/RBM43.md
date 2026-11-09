---
symbol: "RBM43"
type: "gene"
col: 11587
ensembl_id: "ENSG00000184898"
name: "RNA binding motif protein 43"
location: "2q23.3"
module: 32
arm: "+"
pooled_cpm: 9.09
n_lines_expressing: 46
n_dd_up: 25
n_dd_down: 38
n_dd_up_clean: 22
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 9
direction_downstream: 17
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# RBM43

*RNA binding motif protein 43* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.28× (z +9.6, q 5e-19, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.239× (z -16.6, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMI]] (+0.82, fdr 7e-06, ⚠ same locus), [[PSMB8]] (+0.73, fdr 7e-06), [[TRIM21]] (+0.73, fdr 7e-06), [[PHF11]] (+0.73, fdr 7e-06); moves opposite to [[TCF3]] (-0.65, fdr 1e-05), [[ERCC2]] (-0.60, fdr 4e-05), [[TBC1D16]] (-0.59, fdr 3e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ERAP2]] → it (grade B ⚠); 17 go from it, the strongest it → [[NMI]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.28×** | +9.6 | 5e-19 | 31/43 (HS-578T, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.82×** | +6.9 | 1e-09 | 28/44 (A-172, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.76×** | +6.3 | 5e-08 | 22/41 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +5.4 | 9e-06 | 22/43 (NCI-H2347, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.61×** | +5.1 | 3e-05 | 18/37 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 4e-04 | 15/43 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 4e-04 | 20/44 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +4.5 | 5e-04 | 19/42 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 0.001 | 15/44 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.2 | 0.001 | 13/33 (J82, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.1 | 0.002 | 5/16 (J82, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 14/44 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.002 | 18/44 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.003 | 15/44 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.005 | 12/43 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.005 | 17/44 (PANC-1, A-172, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.011 | 9/44 (HS-578T, KATO III, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.239×** | -16.6 | 0e+00 | 42/44 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.272×** | -15.1 | 0e+00 | 41/43 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.277×** | -14.9 | 0e+00 | 40/44 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.369×** | -11.6 | 9e-29 | 30/40 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.470×** | -8.8 | 2e-16 | 32/43 (LS 180, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.510×** | -7.8 | 6e-13 | 27/44 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.499×** | -7.8 | 7e-13 | 26/34 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -7.6 | 1e-12 | 28/44 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.297×** | -7.4 | 1e-11 | 29/38 (A-172, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.541×** | -7.1 | 5e-11 | 31/44 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.542×** | -7.1 | 6e-11 | 27/44 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.652×** | -7.0 | 1e-10 | 27/44 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.547×** | -7.0 | 1e-10 | 24/42 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.335×** | -6.6 | 1e-09 | 25/44 (A549, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.717×** | -5.5 | 2e-06 | 21/42 (RPMI-7951, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.434×** | -5.1 | 1e-05 | 20/44 (HCT15, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.660×** | -4.8 | 5e-05 | 20/41 (SNU-1, A549, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **0.652×** | -4.8 | 6e-05 | 15/44 (SNU-423, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 1 (1 ⚠) | 7 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.57× (z +8.6) ⚠ position not correctable | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0807× (z -13.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.138× (z -10.8) |
| [[A-172 (line)]] | wt | 22.1 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 5.11× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -14.9) |
| [[A498 (line)]] | wt | 18.7 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 3.58× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -11.8) |
| [[A549 (line)]] | wt | 19.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0996× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -16.4) |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0836× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.107× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 11.6 | 2 | 2 | [[Harringtonine (drug)]] 0.5 µM 4.98× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -10.5) |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0622× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 5.75 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0662× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 5.45 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -10.6) |
| [[RKO (line)]] | wt | 9.54 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.100× (z -10.3) |
| [[C32 (line)]] | wt | 15.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.139× (z -10.5) |
| [[HOP62 (line)]] | alt | 9.33 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0599× (z -14.9) |
| [[HS-578T (line)]] | alt | 12.1 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 7.92× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.132× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 7.27 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.107× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -9.0) |
| [[H4 (line)]] | wt | 8.35 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0603× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 8.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 6.77 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.102× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 4.68 | 0 | 1 | — | [[Peretinoin (drug)]] 0.05 µM 0.0631× (z -8.5) |
| [[PANC-1 (line)]] | alt | 8.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.0) |
| [[SW 900 (line)]] | alt | 6.79 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0956× (z -8.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMI]] | +0.82 | +0.77 / +0.78 | both halves | 7e-06 | ⚠ same locus (8.6 kb, same strand: neighbours can correlate without regulation) |
| [[PSMB8]] | +0.73 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[TRIM21]] | +0.73 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[PHF11]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ERAP2]] | +0.72 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SCAMP1-AS1]] | +0.71 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[IFIT2]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[PARP14]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[DHX58]] | +0.71 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[IFIH1]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[DDX60]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[TRIM5]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF3]] | -0.65 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ERCC2]] | -0.60 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D16]] | -0.59 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[GNB1L]] | -0.59 | -0.49 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERAP2]] | B | ERAP2 activity raises RBM43's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 2.67× lower at baseline in the lines without ERAP2 | 0.012 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[GBP5]] | B | GBP5 activity raises RBM43's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without GBP5 | 0.025 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[CSF1]] | B | CSF1 activity raises RBM43's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 1.87× lower at baseline in the lines without CSF1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[IFI16]] | B | IFI16 activity raises RBM43's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.94× lower at baseline in the lines without IFI16 | 0.042 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[IL15RA]] | B | IL15RA activity raises RBM43's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.84× lower at baseline in the lines without IL15RA | 0.051 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers RBM43's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[GBP3]] | B | GBP3 activity raises RBM43's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without GBP3 | 0.098 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[NMI]] | C | NMI activity raises RBM43's level | lines that do not express NMI (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91; its own permutation p |
| [[APOBEC3F]] | C | APOBEC3F activity raises RBM43's level | lines that do not express APOBEC3F (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without APOBEC3F | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PORCN, HOMER3, UGDH; its own permutation p |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMI]] | C | RBM43 activity raises NMI's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 3.87× lower at baseline in the lines without RBM43 | 0.002 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[HLA-E]] | C | RBM43 activity raises HLA-E's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 3.45× lower at baseline in the lines without RBM43 | 0.003 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[TRIM5]] | C | RBM43 activity raises TRIM5's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without RBM43 | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[WHAMMP2]] | C | RBM43 activity lowers WHAMMP2's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 1.74× higher at baseline in the lines without RBM43 | 0.026 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[GBP3]] | C | RBM43 activity raises GBP3's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 5.66× lower at baseline in the lines without RBM43 | 0.027 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[PAXIP1-AS2]] | C | RBM43 activity raises PAXIP1-AS2's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without RBM43 | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[IL15]] | C | RBM43 activity raises IL15's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 3.91× lower at baseline in the lines without RBM43 | 0.037 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[PSMB8]] | C | RBM43 activity raises PSMB8's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 2.52× lower at baseline in the lines without RBM43 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[IL15RA]] | C | RBM43 activity raises IL15RA's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 3.05× lower at baseline in the lines without RBM43 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[CASP8]] | C | RBM43 activity raises CASP8's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without RBM43 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[HERC6]] | C | RBM43 activity raises HERC6's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without RBM43 | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[UBE2L6]] | C | RBM43 activity raises UBE2L6's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 2.55× lower at baseline in the lines without RBM43 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 53.5); signed map (61.8, 31.8). **Vector** length 100, 24.1% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.53 to 56); *interferon gamma response* (hallmark, mean cos +0.53 to 60); *interferon* (control, mean cos +0.57 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.8 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +5.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.3 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +5.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.4 | -11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.8 | -4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | -3.1 | -3.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:151,247,940-151,261,863 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45645; previously C2orf38 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

UniProt [Q6ZSC3](https://www.uniprot.org/uniprotkb/Q6ZSC3) carries no function annotation.

**Summary**, from NCBI Gene [375287](https://www.ncbi.nlm.nih.gov/gene/375287):

> Predicted to enable RNA binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24790) · Entrez [375287](https://www.ncbi.nlm.nih.gov/gene/375287) · UniProt [Q6ZSC3](https://www.uniprot.org/uniprotkb/Q6ZSC3) · Ensembl [ENSG00000184898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184898)

## Data

Gene col 11587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11587); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11587]; `tensor/DDL_lfc|DDL_z.npy` [11587]; `embed/gene_vectors.npy` [11587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11587 or target_col == 11587). Every well: [[RBM43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
