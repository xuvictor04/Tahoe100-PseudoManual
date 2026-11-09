---
symbol: "ACP7"
type: "gene"
col: 11449
ensembl_id: "ENSG00000183760"
name: "acid phosphatase 7, tartrate resistant (putative)"
location: "19q13.2"
module: 110
arm: "+"
pooled_cpm: 3.81
n_lines_expressing: 16
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# ACP7

*acid phosphatase 7, tartrate resistant (putative)* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.22× (z +11.6, q 2e-28, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.02× (z +5.1, q 3e-05, up in 5 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.412× (z -6.0, q 9e-07, down in 10 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO2B]] (+0.73, fdr 7e-06), [[LINC01629]] (+0.65, fdr 7e-06), [[CDCP1]] (+0.65, fdr 7e-06); moves opposite to [[TNS3]] (-0.49, fdr 6e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TIAM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.22×** | +11.6 | 2e-28 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.98×** | +10.1 | 2e-21 | 2/10 (A-427, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.87×** | +9.1 | 1e-17 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +5.7 | 2e-06 | 2/10 (PANC-1, A-427) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +5.7 | 2e-06 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +5.1 | 3e-05 | 5/13 (Panc 03.27, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +4.9 | 8e-05 | 2/13 (PANC-1, SW480) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.38×** | +4.5 | 4e-04 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.3 | 0.001 | 0/13 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.009 | 2/13 (SW480, PANC-1) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.48×** | +3.5 | 0.028 | 2/9 (PANC-1, SW480) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.028 | 4/13 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.029 | 6/13 (PANC-1, SW480, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.89×** | +3.3 | 0.036 | 1/11 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.57×** | +3.3 | 0.041 | 2/13 (PANC-1, SW480) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +3.2 | 0.046 | 1/13 (HCT15) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.59×** | +3.1 | 0.060 | 1/13 (SW480) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.05 µM |  | **1.51×** | +3.0 | 0.076 | 1/13 (NCI-H23) | inconsistent across doses |  |
| [[Neratinib (drug)]] 0.05 µM |  | **1.51×** | +3.0 | 0.076 | 1/13 (A-427) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.50×** | +3.0 | 0.076 | 0/11 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11449.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.412×** | -6.0 | 9e-07 | 10/14 (NCI-H23, RKO, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.556×** | -4.4 | 0.003 | 10/14 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.640×** | -4.0 | 0.011 | 11/13 (NCI-H23, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.681×** | -4.0 | 0.011 | 7/13 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.878× | -3.6 | 0.032 | 4/14 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | 0.429× | -3.3 | 0.11 | 6/13 (RKO, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Encorafenib (drug)]] 5 µM |  | 0.438× | -3.2 | 0.12 | 4/13 (NCI-H23, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 49.1 | 0 | 23 (9 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.202× (z -27.8) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -15.7) |
| [[RKO (line)]] | wt | 31.9 | 0 | 15 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.137× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0607× (z -13.5) |
| [[A-427 (line)]] | wt | 19.4 | 0 | 5 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0877× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.148× (z -9.4) |
| [[HOP62 (line)]] | alt | 4.75 | 0 | 5 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.327× (z -13.4) ⚠ position not correctable · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.0227× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 6.59 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0916× (z -9.9) ⚠ transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -9.1) |
| [[PANC-1 (line)]] | alt | 9.74 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 14.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0244× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0257× (z -8.9) |
| [[SW480 (line)]] | alt | 3.52 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0457× (z -11.5) |
| [[A-172 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO2B]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[LINC01629]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[CDCP1]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ITGB1-DT]] | +0.61 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[ELK3]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TOMM34]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PXN]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[NTSR1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SLC4A7]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS3]] | -0.49 | -0.48 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity raises ACP7's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; shared targets |
| [[LINC02454]] | B | LINC02454 activity raises ACP7's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 2.15× lower at baseline in the lines without LINC02454 | 0.031 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ACP7's level | compounds that target MAP2K1: 2 of 4 lower it (Binimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ARHGAP22]] | B | ARHGAP22 activity raises ACP7's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without ARHGAP22 | 0.078 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[TNS3]] | B | TNS3 activity lowers ACP7's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 2.06× higher at baseline in the lines without TNS3 | 0.093 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[WT1-AS]] | C | WT1-AS activity raises ACP7's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 2.17× lower at baseline in the lines without WT1-AS | 0.039 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TIAM1]] | B | ACP7 activity raises TIAM1's level | lines that do not express ACP7 (34) vs lines expressing it (16) | 1.88× lower at baseline in the lines without ACP7 | 0.086 | ⚠ within organs, on part of the lines; also absent: FGF20, ONECUT3, GPR87 |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.2, 4.0); signed map (5.5, 46.6). **Vector** length 61.9, 21.2% of its response variance represented; |z| ≥ 3 in 465 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +1.7 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +3.4 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | acid phosphatase 7, tartrate resistant (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,083,913-39,111,493 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16165, PAPL1, PAPL |
| Gene groups (HGNC) | Acid phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZNF0](https://www.uniprot.org/uniprotkb/Q6ZNF0) (Acid phosphatase type 7):

> Putative metallophosphoesterase belonging to the purple acid phosphatase family that catalyzes the hydrolysis of phosphate esters to alcohol and phosphate under acidic conditions.

**Summary**, from NCBI Gene [390928](https://www.ncbi.nlm.nih.gov/gene/390928):

> Purple acid phosphatases (PAPs), including PAPL, are a family of binuclear metallohydrolases that have been identified in plants, animals, and fungi (Flanagan et al., 2006 [PubMed 16793224]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:33781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33781) · Entrez [390928](https://www.ncbi.nlm.nih.gov/gene/390928) · UniProt [Q6ZNF0](https://www.uniprot.org/uniprotkb/Q6ZNF0) · Ensembl [ENSG00000183760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183760)

## Data

Gene col 11449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11449); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11449]; `tensor/DDL_lfc|DDL_z.npy` [11449]; `embed/gene_vectors.npy` [11449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11449 or target_col == 11449). Every well: [[ACP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
