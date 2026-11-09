---
symbol: "ATXN7L2"
type: "gene"
col: 8555
ensembl_id: "ENSG00000162650"
name: "ataxin 7 like 2"
location: "1p13.3"
module: 96
arm: "+"
pooled_cpm: 3.48
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# ATXN7L2

*ataxin 7 like 2* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +8.8, q 1e-15, up in 21 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.470× (z -7.7, q 7e-12, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRSF6]] (+0.74, fdr 7e-06), [[TRMO]] (+0.65, fdr 1e-05), [[PIGO]] (+0.65, fdr 7e-06); moves opposite to [[HYCC2]] (-0.69, fdr 7e-06), [[PDCD10]] (-0.56, fdr 1e-05), [[TBC1D12]] (-0.54, fdr 1e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +8.8 | 1e-15 | 21/39 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +5.2 | 5e-05 | 15/46 (LoVo, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +4.3 | 0.002 | 1/11 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +4.3 | 0.002 | 6/46 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.003 | 9/44 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.27×** | +3.6 | 0.027 | 5/45 (LoVo, H4, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.027 | 12/38 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.36× | +3.1 | 0.12 | 7/19 (PANC-1, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.36× | +3.1 | 0.12 | 6/42 (H4, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.12 | 5/43 (LS 180, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.470×** | -7.7 | 7e-12 | 21/37 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.497×** | -7.4 | 3e-11 | 26/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -6.9 | 9e-10 | 20/38 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.574×** | -5.9 | 6e-07 | 19/38 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -5.7 | 1e-06 | 17/35 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.620×** | -5.1 | 4e-05 | 15/46 (C-33 A, J82, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.631×** | -4.9 | 8e-05 | 8/46 (RKO, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.672×** | -4.2 | 0.002 | 11/45 (RKO, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.800×** | -3.4 | 0.047 | 6/45 (A-427, LOX-IMVI, …) | top dose only | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **0.736×** | -3.3 | 0.063 | 11/46 (A549, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -9.9) |
| [[RKO (line)]] | wt | 9.47 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0835× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 2.51 | 0 | 1 | — | [[Voriconazole (drug)]] 0.5 µM 0.0645× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 5.10 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0852× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 2.72 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0749× (z -10.2) |
| [[A-172 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF6]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[TRMO]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PIGO]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[DUS3L]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[NCDN]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[EPC2]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PUF60]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[WDR6]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SARS2]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[DTX3]] | +0.60 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CELSR3]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SRCAP]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYCC2]] | -0.69 | -0.70 / -0.59 | both halves | 7e-06 |  |
| [[PDCD10]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TBC1D12]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.53 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[GAPVD1]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[IKBIP]] | -0.53 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ATP5PF]] | -0.53 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[CACUL1]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[HEBP1]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PPP2R5A]] | -0.52 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[PPP2R5E]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ATXN7L2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers ATXN7L2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RRN3P1]] | B | RRN3P1 activity lowers ATXN7L2's level | lines that do not express RRN3P1 (9) vs lines expressing it (41) | 1.15× higher at baseline in the lines without RRN3P1 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes |
| [[HDAC6]] | B | HDAC6 activity raises ATXN7L2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.4, -20.9); signed map (8.4, -35.8). **Vector** length 56.5, 7.17% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +2.4 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.4 | -2.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 7 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,483,479-109,492,804 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC46534, FLJ00381 |
| Gene groups (HGNC) | Ataxin 7 family |
| Matched by | ensembl_id |

UniProt [Q5T6C5](https://www.uniprot.org/uniprotkb/Q5T6C5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28713) · Entrez [127002](https://www.ncbi.nlm.nih.gov/gene/127002) · UniProt [Q5T6C5](https://www.uniprot.org/uniprotkb/Q5T6C5) · Ensembl [ENSG00000162650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162650)

## Data

Gene col 8555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8555); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8555]; `tensor/DDL_lfc|DDL_z.npy` [8555]; `embed/gene_vectors.npy` [8555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8555 or target_col == 8555). Every well: [[ATXN7L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN7L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
