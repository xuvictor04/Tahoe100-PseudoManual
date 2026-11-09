---
symbol: "AZU1"
type: "gene"
col: 10226
ensembl_id: "ENSG00000172232"
name: "azurocidin 1"
location: "19p13.3"
module: 53
arm: "+"
pooled_cpm: 2.67
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/053", "written"]
generated_by: "tahoemap"
---

# AZU1

*azurocidin 1* — 19p13.3

> [!summary] In one line
> AZU1 encodes azurocidin (CAP37, heparin-binding protein), an antibacterial and chemotactic protein stored in the azurophil granules of neutrophils.

## What it is

Azurocidin is made in promyelocytes and stored in primary granules for release on activation. It folds like an elastase-family serine protease but lacks the catalytic serine and histidine, so it is not an enzyme. It binds heparin and lipopolysaccharide, kills Gram-negative bacteria, attracts monocytes, and increases endothelial permeability — the property behind its use as a sepsis marker. Expression is essentially restricted to bone marrow; the gene lies at 19p13.3 among other azurophil-granule protease genes. No function is established outside the neutrophil lineage, and no link to p53 or to membrane repair is reported.

## What is uncertain

Essentially everything that matters here. The transcript sits close to the detection floor, and a promyelocyte-restricted gene reading as weakly present across a pooled cancer-line panel is as easily explained by ambient RNA, or by reads shared with its near-identical neighbours at 19p13.3, as by real expression. Nothing in this design separates a real association from a correlation driven by a few lines, by sequencing depth or by ambient RNA. Treat it as a lead for a targeted assay, not a finding.

## References

- Pereira et al., 1990, Journal of Clinical Investigation — characterised CAP37 as a neutrophil-derived chemotactic factor with monocyte specificity.
- Gautam et al., 2001, Nature Medicine — showed heparin-binding protein released from neutrophils causes endothelial hyperpermeability.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.50× (z +14.3, q 1e-43, up in 24 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.464× (z -5.2, q 1e-04, down in 17 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRAMD2A]] (+0.82, fdr 7e-06), [[TRIM72]] (+0.79, fdr 7e-06), [[CPT1C]] (+0.78, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CHD5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.50×** | +14.3 | 1e-43 | 24/27 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.17×** | +11.0 | 1e-25 | 23/32 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +5.5 | 9e-06 | 2/3 (MIA PaCa-2, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +4.9 | 1e-04 | 10/30 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +4.8 | 1e-04 | 7/22 (SW480, HCT15, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.8 | 1e-04 | 6/41 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +4.4 | 1e-03 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.80×** | +3.7 | 0.018 | 2/14 (HEC-1-A, A-172) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +3.6 | 0.020 | 3/34 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.021 | 2/40 (PANC-1, SW480) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.027 | 8/38 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **2.65×** | +3.4 | 0.029 | 1/13 (MIA PaCa-2) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +3.4 | 0.032 | 3/31 (SW480, HOP62, …) | top dose only | position effect removed |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.60×** | +3.2 | 0.062 | 4/40 (HepG2/C3A, SK-MEL-2, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.60×** | +3.1 | 0.062 | 4/15 (A-172, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Raltitrexed (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.074 | 4/43 (Panc 03.27, A498, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.38×** | +3.0 | 0.074 | 0/19 | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10226.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.464×** | -5.2 | 1e-04 | 17/33 (HEC-1-A, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.642×** | -4.2 | 0.006 | 12/41 (PANC-1, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.597×** | -3.5 | 0.091 | 14/36 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (drug)]] 5 µM |  | 0.616× | -3.3 | 0.15 | 10/34 (LS 180, J82, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.617× | -3.0 | 0.27 | 6/41 (LoVo, AsPC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.87 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.174× (z -9.6) |
| [[A-427 (line)]] | wt | 5.21 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0885× (z -8.7) |
| [[LoVo (line)]] | wt | 3.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 0.952 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +8.5) | — |
| [[A-172 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.928 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.667 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.995 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRAMD2A]] | +0.82 | +0.77 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.79 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.78 | +0.83 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[MIR9-1HG]] | +0.76 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[CSPG5]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[KIF17]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[PYGM]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[HPX]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[CHADL]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.71 | +0.69 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD5]] | B | CHD5 activity raises AZU1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.45× lower at baseline in the lines without CHD5 | 0.018 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[SSC5D]] | B | SSC5D activity raises AZU1's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without SSC5D | 0.026 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers AZU1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EFNA2]] | B | EFNA2 activity raises AZU1's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without EFNA2 | 0.074 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |
| [[FES]] | B | FES activity lowers AZU1's level | lines that do not express FES (11) vs lines expressing it (39) | 1.64× higher at baseline in the lines without FES | 0.096 | ⚠ within organs, on part of the lines; also absent: RBPMS, GLRX, SEMA4A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.6, -16.1); signed map (16.8, 13.0). **Vector** length 65.0, 11.3% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +14.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | azurocidin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:825,097-832,018 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AZU, CAP37, AZAMP, HBP, NAZC, HUMAZUR |
| Gene groups (HGNC) | Granule associated serine proteases of immune defence |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P20160](https://www.uniprot.org/uniprotkb/P20160) (Azurocidin):

> This is a neutrophil granule-derived antibacterial and monocyte- and fibroblast-specific chemotactic glycoprotein. Binds heparin. The cytotoxic action is limited to many species of Gram-negative bacteria; this specificity may be explained by a strong affinity of the very basic N-terminal half for the negatively charged lipopolysaccharides that are unique to the Gram-negative bacterial outer envelope. It may play a role in mediating recruitment of monocytes in the second wave of inflammation. …

**Summary**, from NCBI Gene [566](https://www.ncbi.nlm.nih.gov/gene/566):

> Azurophil granules, specialized lysosomes of the neutrophil, contain at least 10 proteins implicated in the killing of microorganisms. This gene encodes a preproprotein that is proteolytically processed to generate a mature azurophil granule antibiotic protein, with monocyte chemotactic and antimicrobial activity. It is also an important multifunctional inflammatory mediator. This encoded protein is a member of the serine protease gene family but it is not a serine proteinase, because the …

**Accessions** — [HGNC:913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:913) · Entrez [566](https://www.ncbi.nlm.nih.gov/gene/566) · UniProt [P20160](https://www.uniprot.org/uniprotkb/P20160) · Ensembl [ENSG00000172232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172232)

## Data

Gene col 10226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10226); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10226]; `tensor/DDL_lfc|DDL_z.npy` [10226]; `embed/gene_vectors.npy` [10226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10226 or target_col == 10226). Every well: [[AZU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/AZU1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
