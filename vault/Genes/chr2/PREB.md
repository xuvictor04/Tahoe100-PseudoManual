---
symbol: "PREB"
type: "gene"
col: 6118
ensembl_id: "ENSG00000138073"
name: "prolactin regulatory element binding"
location: "2p23.3"
module: 49
arm: "+"
pooled_cpm: 11.77
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# PREB

*prolactin regulatory element binding* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.24× (z +9.6, q 3e-19, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.60× (z +5.4, q 9e-06, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.400× (z -11.0, q 3e-25, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED8]] (+0.71, fdr 1e-05), [[SPRYD3]] (+0.66, fdr 1e-05), [[TIMM17A]] (+0.65, fdr 1e-05); moves opposite to [[FAM81A]] (-0.58, fdr 1e-05), [[LAMTOR5-AS1]] (-0.55, fdr 2e-04), [[ZNF789]] (-0.52, fdr 1e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.24×** | +9.6 | 3e-19 | 40/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.80×** | +7.0 | 6e-10 | 32/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.75×** | +6.7 | 4e-09 | 28/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +5.4 | 9e-06 | 27/41 (SW 900, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.4 | 9e-06 | 23/46 (NCI-H1573, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +5.3 | 1e-05 | 26/43 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.57×** | +5.2 | 2e-05 | 11/21 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.0 | 4e-05 | 4/48 (COLO 205, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +3.7 | 0.015 | 12/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.73× | +3.1 | 0.10 | 7/26 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | 1.30× | +3.0 | 0.12 | 15/35 (A-172, J82, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.400×** | -11.0 | 3e-25 | 40/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.452×** | -9.5 | 5e-19 | 37/45 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.465×** | -9.2 | 8e-18 | 38/47 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.607×** | -8.4 | 4e-15 | 30/45 (RPMI-7951, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.540×** | -7.4 | 2e-11 | 32/46 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.311×** | -6.6 | 3e-09 | 29/47 (KATO III, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.714×** | -4.0 | 0.004 | 14/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.523×** | -3.7 | 0.017 | 16/43 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.747×** | -3.5 | 0.030 | 18/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -11.5) |
| [[KATO III (line)]] | alt | 23.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -12.4) |
| [[BT-474 (line)]] | alt | 9.89 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.121× (z -8.9) |
| [[LoVo (line)]] | wt | 13.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0363× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.257× (z -8.8) |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -9.8) |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0903× (z -10.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 7.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0359× (z -16.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 7.41 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0824× (z -9.2) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 7.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0789× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.4) |
| [[RKO (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -13.9) |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -9.4) |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -11.5) |
| [[SW48 (line)]] | wt | 10.6 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0722× (z -9.0) |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED8]] | +0.71 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SPRYD3]] | +0.66 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TIMM17A]] | +0.65 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[MRPL17]] | +0.65 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SRPRB]] | +0.64 | +0.69 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[YIF1A]] | +0.60 | +0.45 / +0.66 | both halves | 3e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 584 |
| [[ARL1]] | +0.60 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[GMPPA]] | +0.59 | +0.53 / +0.48 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[MRPL2]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TMEM214]] | +0.58 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[MRPL55]] | +0.58 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[FAM98A]] | +0.57 | +0.58 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM81A]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[LAMTOR5-AS1]] | -0.55 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[ZNF789]] | -0.52 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[KMT2E-AS1]] | -0.49 | -0.29 / -0.31 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PREB's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.9, -30.2); signed map (-55.5, 11.3). **Vector** length 76.0, 14.7% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +1.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.4 | +9.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -11.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -9.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | prolactin regulatory element binding |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,130,756-27,134,666 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEC12 |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, ADIPOGENESIS |
| Reactome | 12 pathways, smallest: Cargo concentration in the ER; XBP1(S) activates chaperone genes; IRE1alpha activates chaperones |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCU5](https://www.uniprot.org/uniprotkb/Q9HCU5) (Guanine nucleotide-exchange factor SEC12):

> Guanine nucleotide exchange factor (GEF) that regulates the assembly of the coat protein complex II/COPII in endoplasmic reticulum (ER) to Golgi vesicle-mediated transport. Selectively activates SAR1A and SAR1B by promoting the exchange of guanosine diphosphate (GDP) for guanosine triphosphate (GTP) in these small GTPases. In their activated GTP-bound state, SAR1A and SAR1B insert into the membrane of the endoplasmic reticulum where they recruit the remainder of the coat protein complex …

**Summary**, from NCBI Gene [10113](https://www.ncbi.nlm.nih.gov/gene/10113):

> This gene encodes a protein that specifically binds to a Pit1-binding element of the prolactin (PRL) promoter. This protein may act as a transcriptional regulator and is thought to be involved in some of the developmental abnormalities observed in patients with partial trisomy 2p. This gene overlaps the abhydrolase domain containing 1 (ABHD1) gene on the opposite strand. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9356) · Entrez [10113](https://www.ncbi.nlm.nih.gov/gene/10113) · UniProt [Q9HCU5](https://www.uniprot.org/uniprotkb/Q9HCU5) · Ensembl [ENSG00000138073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138073)

## Data

Gene col 6118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6118); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6118]; `tensor/DDL_lfc|DDL_z.npy` [6118]; `embed/gene_vectors.npy` [6118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6118 or target_col == 6118). Every well: [[PREB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PREB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
