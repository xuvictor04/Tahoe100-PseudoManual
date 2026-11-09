---
symbol: "COX11"
type: "gene"
col: 9269
ensembl_id: "ENSG00000166260"
name: "cytochrome c oxidase copper chaperone COX11"
location: "17q22"
module: 25
arm: "+"
pooled_cpm: 17.29
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# COX11

*cytochrome c oxidase copper chaperone COX11* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.21× (z +20.5, q 0e+00, up in 40 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +7.7, q 2e-12, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.679× (z -5.5, q 2e-05, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS6]] (+0.72, fdr 7e-06), [[SNX17]] (+0.71, fdr 7e-06), [[PNPO]] (+0.68, fdr 7e-06); moves opposite to [[POLR2J4]] (-0.69, fdr 7e-06), [[INAFM1]] (-0.62, fdr 3e-05), [[TTLL3]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.21×** | +20.5 | 0e+00 | 40/42 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +18.8 | 0e+00 | 31/32 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +13.6 | 4e-40 | 34/36 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.7 | 2e-12 | 27/48 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.3 | 4e-11 | 32/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.69×** | +7.1 | 8e-11 | 30/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.68×** | +7.1 | 8e-11 | 30/46 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +6.5 | 6e-09 | 28/48 (A-427, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.53×** | +6.1 | 7e-08 | 28/47 (BT-474, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.49×** | +5.7 | 8e-07 | 27/47 (BT-474, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.46×** | +5.4 | 3e-06 | 26/47 (BT-474, A498, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.48×** | +5.4 | 3e-06 | 26/45 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.45×** | +5.3 | 5e-06 | 22/44 (CFPAC-1, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 6e-06 | 23/47 (HEC-1-A, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +4.8 | 5e-05 | 22/47 (BT-474, SK-MEL-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.5 | 3e-04 | 23/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.002 | 16/47 (BT-474, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.003 | 14/47 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.019 | 12/45 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.031 | 13/47 (NCI-H1792, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.1 | 0.043 | 12/48 (A498, HepG2/C3A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.043 | 8/48 (A498, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.043 | 13/45 (A549, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.059 | 10/47 (BT-474, A-427, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.49×** | +2.9 | 0.069 | 4/46 (SW480, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -5.5 | 2e-05 | 24/47 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -4.6 | 1e-03 | 23/47 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.730×** | -4.5 | 0.001 | 20/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -4.1 | 0.006 | 19/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.761×** | -3.9 | 0.010 | 20/47 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.76× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 18.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.57× (z +14.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.316× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 23.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.65× (z +17.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 13.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 19.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 29.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +14.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +10.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 14.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +12.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 21.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +9.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.172× (z -10.2) |
| [[PANC-1 (line)]] | alt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 18.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.79× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +10.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +10.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.107× (z -8.8) |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.122× (z -9.4) |
| [[Hs 766T (line)]] | wt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +8.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0963× (z -9.7) |
| [[J82 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.72× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0777× (z -9.9) |
| [[A-427 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS6]] | +0.72 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SNX17]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PNPO]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[TSPAN6]] | +0.68 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ATRAID]] | +0.67 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[RBBP9]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[DR1]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ATP5F1A]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[CDKN2AIPNL]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TOP2B]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MANEA]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J4]] | -0.69 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.62 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TTLL3]] | -0.60 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[DRD4]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[BIN3]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.59 | -0.59 / -0.51 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UBE2CP5]] | -0.58 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[RABGEF1]] | -0.58 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[TMEM106A]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[LIPE-AS1]] | -0.57 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[C19orf25]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[LINC02804]] | -0.56 | -0.18 / -0.58 | ⚠ one half (not replicated) | 1e-03 |  |
| [[EEF1D]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZNF611]] | -0.56 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COX11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLS3]] | C | PLS3 activity lowers COX11's level | lines that do not express PLS3 (4) vs lines expressing it (46) | 1.65× higher at baseline in the lines without PLS3 | 0.094 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.1, -18.5); signed map (-18.5, -40.9). **Vector** length 66.9, 12.1% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +20.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +18.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +13.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -0.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.5 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase copper chaperone COX11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:54,951,902-54,968,703 (-) |
| Ensembl biotype | protein_coding |
| Also known as | COX11P |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6N1](https://www.uniprot.org/uniprotkb/Q9Y6N1) (Cytochrome c oxidase assembly protein COX11, mitochondrial):

> Assembly factor for cytochrome c oxidase (respiratory chain complex IV, CIV). Probably acts as a metallochaperone that delivers copper to the copper B site of COX1.

**Summary**, from NCBI Gene [1353](https://www.ncbi.nlm.nih.gov/gene/1353):

> Cytochrome c oxidase (COX), the terminal component of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. This component is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, and the nuclear-encoded subunits may function in the regulation and assembly of the complex. This nuclear …

**Accessions** — [HGNC:2261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2261) · Entrez [1353](https://www.ncbi.nlm.nih.gov/gene/1353) · UniProt [Q9Y6N1](https://www.uniprot.org/uniprotkb/Q9Y6N1) · Ensembl [ENSG00000166260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166260)

## Data

Gene col 9269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9269); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9269]; `tensor/DDL_lfc|DDL_z.npy` [9269]; `embed/gene_vectors.npy` [9269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9269 or target_col == 9269). Every well: [[COX11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
