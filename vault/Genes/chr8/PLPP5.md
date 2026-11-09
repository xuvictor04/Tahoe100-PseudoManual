---
symbol: "PLPP5"
type: "gene"
col: 7196
ensembl_id: "ENSG00000147535"
name: "phospholipid phosphatase 5"
location: "8p11.23"
module: 49
arm: "+"
pooled_cpm: 25.75
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# PLPP5

*phospholipid phosphatase 5* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +9.5, q 1e-18, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.488× (z -9.0, q 1e-16, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERP1]] (+0.73, fdr 7e-06), [[C14orf28]] (+0.69, fdr 7e-06), [[BET1]] (+0.69, fdr 7e-06); moves opposite to [[RAB10]] (-0.55, fdr 3e-05), [[SERBP1]] (-0.54, fdr 7e-05), [[TAF1B]] (-0.53, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.5 | 1e-18 | 37/47 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +9.2 | 1e-17 | 42/45 (AsPC-1, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +8.0 | 3e-13 | 37/48 (A-427, SNU-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.012 | 20/46 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.8 | 0.016 | 23/43 (RKO, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.026 | 20/46 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.30× | +3.2 | 0.11 | 16/35 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vilanterol (drug)]] 5 µM |  | 1.20× | +3.1 | 0.15 | 13/48 (HEC-1-A, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.488×** | -9.0 | 1e-16 | 35/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.520×** | -8.2 | 7e-14 | 33/48 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.542×** | -7.7 | 3e-12 | 34/48 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.379×** | -6.4 | 3e-08 | 34/48 (SNU-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -5.7 | 2e-06 | 31/46 (RPMI-7951, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.703×** | -4.4 | 9e-04 | 26/48 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.740×** | -3.8 | 0.013 | 18/48 (KATO III, HCT15, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.730×** | -3.7 | 0.013 | 20/47 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.808×** | -3.6 | 0.020 | 20/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.059 | 20/46 (H4, SNU-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 52.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.4) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.442× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -12.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.350× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.7) | — |
| [[A-172 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERP1]] | +0.73 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[C14orf28]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[BET1]] | +0.69 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[DNAJB9]] | +0.66 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[ZFPL1]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SLC15A2]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PCGF3-AS1]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.64 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[ZNF547]] | +0.64 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TAF12]] | +0.64 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[SLC33A1]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[IFT20]] | +0.64 | +0.73 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB10]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SERBP1]] | -0.54 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[TAF1B]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[DHX9]] | -0.52 | -0.40 / -0.60 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PLPP5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PLPP5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[POLR3D]] | C | POLR3D's natural level strengthens PLPP5's drug response | POLR3D's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.48; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.1, -38.3); signed map (0.2, 2.4). **Vector** length 106, 27.1% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.7 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.4 | -6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -5.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.7 | -8.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.6 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -3.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | phospholipid phosphatase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:38,263,130-38,269,243 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HTPAP, DPPL1; previously PPAPDC1B |
| Gene groups (HGNC) | Phospholipid phosphatases |
| Reactome | 3 pathways, smallest: Role of phospholipids in phagocytosis; Fcgamma receptor (FCGR) dependent phagocytosis; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEB5](https://www.uniprot.org/uniprotkb/Q8NEB5) (Phospholipid phosphatase 5):

> Magnesium-independent phospholipid phosphatase with broad substrate specificity. Preferentially catalyzes the conversion of diacylglycerol pyrophosphate into phosphatidate but can also act on phosphatidate and lysophosphatidate. Phospholipid phosphatases are involved in both the synthesis of lipids and the generation or degradation of lipid-signaling molecules.

**Summary**, from NCBI Gene [84513](https://www.ncbi.nlm.nih.gov/gene/84513):

> Enables diacylglycerol diphosphate phosphatase activity and phosphatidate phosphatase activity. Involved in phospholipid dephosphorylation. Predicted to be located in cytoplasm and plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25026) · Entrez [84513](https://www.ncbi.nlm.nih.gov/gene/84513) · UniProt [Q8NEB5](https://www.uniprot.org/uniprotkb/Q8NEB5) · Ensembl [ENSG00000147535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147535)

## Data

Gene col 7196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7196); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7196]; `tensor/DDL_lfc|DDL_z.npy` [7196]; `embed/gene_vectors.npy` [7196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7196 or target_col == 7196). Every well: [[PLPP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLPP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
