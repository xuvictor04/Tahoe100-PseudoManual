---
symbol: "PLD5"
type: "gene"
col: 11095
ensembl_id: "ENSG00000180287"
name: "phospholipase D family member 5"
location: "1q43"
module: 165
arm: "+"
pooled_cpm: 4.02
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# PLD5

*phospholipase D family member 5* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.75× (z +22.1, q 0e+00, up in 22 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.172×); [[Demeclocycline (drug)]] 0.05 µM in 1 line (PANC-1 0.0506×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBFOX3]] (+0.75, fdr 7e-06), [[LINC02511]] (+0.73, fdr 7e-06), [[MTUS2]] (+0.72, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GRID1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.75×** | +22.1 | 0e+00 | 22/27 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.97×** | +19.6 | 0e+00 | 39/44 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.01×** | +15.6 | 0e+00 | 2/4 (NCI-H460, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.78×** | +14.5 | 1e-45 | 22/26 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.16×** | +14.3 | 3e-44 | 10/13 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.43×** | +11.4 | 2e-28 | 2/6 (SW 900, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.94×** | +10.8 | 2e-25 | 23/33 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +8.7 | 3e-16 | 12/27 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +8.3 | 6e-15 | 13/26 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.20×** | +7.9 | 1e-13 | 20/38 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +7.2 | 2e-11 | 16/36 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +6.3 | 1e-08 | 6/25 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +6.0 | 9e-08 | 6/11 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.81×** | +5.9 | 1e-07 | 17/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.3 | 4e-06 | 8/44 (NCI-H460, A498, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.88×** | +4.5 | 2e-04 | 5/19 (NCI-H1573, SNU-423, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +4.4 | 3e-04 | 11/43 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.2 | 6e-04 | 9/44 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.001 | 8/40 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.001 | 9/37 (NCI-H1573, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11095.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.172×); [[Demeclocycline (drug)]] 0.05 µM in 1 line (PANC-1 0.0506×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -3.7 | 0.11 | 13/47 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Uridine (drug)]] 0.05 µM |  | 0.715× | -3.4 | 0.18 | 3/44 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.720× | -3.3 | 0.18 | 1/45 (HOP62) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.801× | -3.2 | 0.22 | 2/45 (Panc 03.27, LOX-IMVI) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.8 | 15 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 18.9× (z +19.0) | — |
| [[PANC-1 (line)]] | alt | 1.31 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 10.4× (z +10.4) | [[Demeclocycline (drug)]] 0.05 µM 0.0506× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 6.74 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 18.3× (z +13.8) | — |
| [[A-427 (line)]] | wt | 5.64 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.0× (z +11.9) | — |
| [[A498 (line)]] | wt | 1.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.59× (z +9.0) | — |
| [[A549 (line)]] | wt | 66.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.9) |
| [[BT-474 (line)]] | alt | 2.92 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 24.6× (z +10.2) | — |
| [[C32 (line)]] | wt | 1.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 6.56 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.21× (z +8.9) | — |
| [[A-172 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBFOX3]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[LINC02511]] | +0.73 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[CDH23]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[DLGAP2]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.68 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[RYR3]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[XKR4]] | +0.67 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[DACH2]] | +0.67 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[RELN]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRID1]] | B | GRID1 activity raises PLD5's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without GRID1 | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PLD5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.745). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.0, 31.2); signed map (30.6, 18.1). **Vector** length 60.5, 9.28% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +19.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +11.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase D family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:242,082,986-242,524,697 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40773 |
| Gene groups (HGNC) | Phospholipases |
| Matched by | ensembl_id |

UniProt [Q8N7P1](https://www.uniprot.org/uniprotkb/Q8N7P1) carries no function annotation.

**Summary**, from NCBI Gene [200150](https://www.ncbi.nlm.nih.gov/gene/200150):

> Predicted to enable catalytic activity. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26879) · Entrez [200150](https://www.ncbi.nlm.nih.gov/gene/200150) · UniProt [Q8N7P1](https://www.uniprot.org/uniprotkb/Q8N7P1) · Ensembl [ENSG00000180287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180287)

## Data

Gene col 11095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11095); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11095]; `tensor/DDL_lfc|DDL_z.npy` [11095]; `embed/gene_vectors.npy` [11095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11095 or target_col == 11095). Every well: [[PLD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
