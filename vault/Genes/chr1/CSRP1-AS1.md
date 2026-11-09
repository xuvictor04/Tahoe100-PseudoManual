---
symbol: "CSRP1-AS1"
type: "gene"
col: 13403
ensembl_id: "ENSG00000224536"
name: "CSRP1 antisense RNA 1"
location: "1q32.1"
module: 63
arm: "+"
pooled_cpm: 3.85
n_lines_expressing: 45
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# CSRP1-AS1

*CSRP1 antisense RNA 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.01× (z +7.1, q 8e-10, up in 5 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.55× (z +4.4, q 0.001, up in 9 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.455× (z -8.0, q 1e-12, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDUA]] (+0.55, fdr 2e-05), [[LINC03009]] (+0.53, fdr 5e-05), [[SLC48A1]] (+0.52, fdr 4e-05); moves opposite to [[CCDC142]] (-0.47, fdr 8e-05), [[MRPS36]] (-0.46, fdr 1e-04, ⚠ MRPS36 in the vector space only through flagged drug-doses), [[B9D2]] (-0.45, fdr 4e-05), [[UPF2]] (-0.44, fdr 1e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +7.1 | 8e-10 | 5/21 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.7 | 6e-09 | 1/3 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +6.0 | 4e-07 | 3/6 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +5.9 | 6e-07 | 11/41 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +4.4 | 0.001 | 9/39 (NCI-H460, SW480, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.026 | 5/39 (SW 900, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.027 | 8/39 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.037 | 1/36 (A-427) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.4 | 0.040 | 1/16 (A549) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.044 | 5/39 (NCI-H1792, HEC-1-A, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +3.2 | 0.065 | 2/34 (NCI-H460, NCI-H23) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.455×** | -8.0 | 1e-12 | 23/36 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.465×** | -7.7 | 3e-12 | 25/38 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.499×** | -7.0 | 4e-10 | 22/40 (C32, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.528×** | -6.4 | 2e-08 | 20/36 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.556×** | -5.9 | 4e-07 | 17/29 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.579×** | -5.5 | 3e-06 | 18/37 (BT-474, NCI-H2030, …) | inconsistent across doses |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **0.606×** | -4.7 | 2e-04 | 9/28 (A549, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -4.6 | 3e-04 | 12/38 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.632×** | -4.5 | 5e-04 | 13/36 (PANC-1, SK-MEL-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.734×** | -4.4 | 6e-04 | 15/32 (C32, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -4.4 | 6e-04 | 15/37 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.633×** | -4.4 | 6e-04 | 15/33 (KATO III, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.659×** | -4.2 | 0.001 | 12/29 (C32, NCI-H2347, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.454×** | -4.2 | 0.001 | 14/27 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.681×** | -3.9 | 0.004 | 10/40 (HepG2/C3A, SW48, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -3.7 | 0.007 | 14/27 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -3.6 | 0.009 | 15/30 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 8.94 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.113× (z -8.5) |
| [[PANC-1 (line)]] | alt | 5.45 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.139× (z -9.4) |
| [[LoVo (line)]] | wt | 10.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.170× (z -9.1) |
| [[A-427 (line)]] | wt | 9.96 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.165× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 6.54 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 6.07 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0618× (z -9.7) |
| [[SW 900 (line)]] | alt | 4.10 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.5 µM 0.0416× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 3.35 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.128× (z -8.8) |
| [[A-172 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDUA]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[LINC03009]] | +0.53 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SLC48A1]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ULBP1]] | +0.51 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[DNAJC10]] | +0.51 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[DTD1]] | +0.49 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[TSEN15]] | +0.48 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[CLGN]] | +0.47 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[TMEM170B]] | +0.47 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[PSAT1]] | +0.46 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[TCEA1]] | +0.46 | +0.36 / +0.45 | both halves | 9e-05 |  |
| [[PSPH]] | +0.46 | +0.41 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC142]] | -0.47 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[MRPS36]] ⚠ | -0.46 | -0.36 / -0.41 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[B9D2]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[UPF2]] | -0.44 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[COX7A2]] ⚠ | -0.44 | -0.35 / -0.40 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[WDR83OS]] ⚠ | -0.44 | -0.35 / -0.44 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[HECTD4]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ATP5PF]] | -0.42 | -0.24 / -0.49 | both halves | 4e-04 |  |
| [[SYNRG]] | -0.42 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[FLJ46284]] | -0.41 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[KBTBD4]] | -0.41 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[EMC3]] | -0.41 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[COX6B1]] | -0.41 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[MRPL32]] | -0.41 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[CHMP5]] | -0.41 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.465). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.3, 46.3); signed map (-25.6, -50.4). **Vector** length 51.6, 7.18% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.8 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.1 | +1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.0 | +2.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.5 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CSRP1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.1 — chr1:201,507,241-201,534,784 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AC096677.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55856) · Entrez [107985246](https://www.ncbi.nlm.nih.gov/gene/107985246) · Ensembl [ENSG00000224536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224536)

## Data

Gene col 13403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13403); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13403]; `tensor/DDL_lfc|DDL_z.npy` [13403]; `embed/gene_vectors.npy` [13403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13403 or target_col == 13403). Every well: [[CSRP1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSRP1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
