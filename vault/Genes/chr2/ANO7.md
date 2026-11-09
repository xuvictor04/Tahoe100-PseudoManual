---
symbol: "ANO7"
type: "gene"
col: 7072
ensembl_id: "ENSG00000146205"
name: "anoctamin 7"
location: "2q37.3"
module: 105
arm: "+"
pooled_cpm: 3.31
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# ANO7

*anoctamin 7* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +7.0, q 2e-09, up in 16 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.288× (z -14.0, q 8e-42, down in 32 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK2]] (+0.63, fdr 1e-05), [[POM121]] (+0.60, fdr 1e-05), [[DDN-AS1]] (+0.59, fdr 1e-05); moves opposite to [[TIMM17B]] (-0.63, fdr 7e-06, ⚠ TIMM17B in the vector space only through flagged drug-doses), [[SPG11]] (-0.60, fdr 2e-05), [[CEP350]] (-0.56, fdr 2e-05), [[CREB3]] (-0.55, fdr 3e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +7.0 | 2e-09 | 16/34 (HEC-1-A, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +4.8 | 4e-04 | 2/8 (HOP62, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.31×** | +4.5 | 0.001 | 10/42 (NCI-H460, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.009 | 6/42 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.009 | 7/38 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.015 | 6/31 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.081 | 3/30 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.32× | +3.2 | 0.10 | 2/15 (NCI-H1792, HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.32× | +3.2 | 0.10 | 2/41 (SK-MEL-2, SW 900) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.30× | +3.1 | 0.13 | 5/41 (SW480, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7072.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.288×** | -14.0 | 8e-42 | 32/39 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.533×** | -10.4 | 7e-23 | 24/32 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.492×** | -8.3 | 2e-14 | 21/31 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -4.2 | 0.004 | 14/41 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.727×** | -3.7 | 0.022 | 10/33 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -3.6 | 0.033 | 8/44 (HepG2/C3A, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.20 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0447× (z -16.5) |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -14.2) |
| [[BT-474 (line)]] | alt | 5.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 2.56 | 0 | 1 | — | [[Filgotinib (drug)]] 0.5 µM 0.0829× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 8.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 9.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 3.75 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -9.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 2.33 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0970× (z -8.7) |
| [[A-172 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK2]] | +0.63 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[POM121]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[DDN-AS1]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[BCL2L2]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SNHG30]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[DOCK7-DT]] | +0.57 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[CRYBB2P1]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RNF4]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TFR2]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[LINC03009]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CTDP1]] | +0.54 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM17B]] ⚠ | -0.63 | -0.58 / -0.60 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SPG11]] | -0.60 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[CEP350]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CREB3]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[MPC1]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[YIF1A]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[DNAL4]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[SLC25A46]] | -0.53 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[THAP5]] | -0.53 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[TIPRL]] | -0.53 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[AKAP9]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MAP9]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TMEM260]] | -0.51 | -0.61 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANO7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers ANO7's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.9, -19.9); signed map (-43.5, 22.0). **Vector** length 48.5, 5.84% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.4 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.0 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -14.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.2 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.8 | -1.0 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -0.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | anoctamin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,188,509-241,225,976 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NGEP, PCANAP5L, IPCA-5; previously PCANAP5, TMEM16G |
| Gene groups (HGNC) | Anoctamins |
| Reactome | 8 pathways, smallest: Induction of Cell-Cell Fusion; Late SARS-CoV-2 Infection Events; Stimuli-sensing channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IWH7](https://www.uniprot.org/uniprotkb/Q6IWH7) (Anoctamin-7):

> Has calcium-dependent phospholipid scramblase activity; scrambles phosphatidylserine, phosphatidylcholine and galactosylceramide (By similarity). Does not exhibit calcium-activated chloride channel (CaCC) activity. May play a role in cell-cell interactions.

**Summary**, from NCBI Gene [50636](https://www.ncbi.nlm.nih.gov/gene/50636):

> This prostate-specific gene encodes a cytoplasmic protein, as well as a polytopic membrane protein which may serve as a target in prostate cancer diagnosis and immunotherapy. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:31677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31677) · Entrez [50636](https://www.ncbi.nlm.nih.gov/gene/50636) · UniProt [Q6IWH7](https://www.uniprot.org/uniprotkb/Q6IWH7) · Ensembl [ENSG00000146205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146205)

## Data

Gene col 7072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7072); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7072]; `tensor/DDL_lfc|DDL_z.npy` [7072]; `embed/gene_vectors.npy` [7072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7072 or target_col == 7072). Every well: [[ANO7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANO7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
