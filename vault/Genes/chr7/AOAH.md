---
symbol: "AOAH"
type: "gene"
col: 5844
ensembl_id: "ENSG00000136250"
name: "acyloxyacyl hydrolase"
location: "7p14.2"
module: 44
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# AOAH

*acyloxyacyl hydrolase* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.30× (z +9.1, q 5e-17, up in 2 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +8.4, q 1e-14, up in 12 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.550× (z -6.8, q 6e-09, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02580]] (+0.64, fdr 8e-06), [[UGT1A1]] (+0.61, fdr 1e-05), [[GPA33]] (+0.61, fdr 1e-05); moves opposite to [[CROCCP3]] (-0.48, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FCGBP]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Futibatinib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +9.1 | 5e-17 | 2/11 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +8.6 | 3e-15 | 3/16 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +8.4 | 1e-14 | 12/32 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +7.7 | 3e-12 | 5/11 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.0 | 4e-10 | 18/40 (SW480, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +6.5 | 6e-09 | 12/39 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +5.0 | 6e-05 | 10/33 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.58×** | +4.1 | 0.003 | 13/42 (LS 180, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.010 | 11/36 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.082 | 6/36 (HepG2/C3A, SHP-77, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5844.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.550×** | -6.8 | 6e-09 | 21/42 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -4.6 | 0.001 | 13/30 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -4.5 | 0.002 | 16/40 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.696×** | -4.1 | 0.005 | 9/41 (AsPC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.702×** | -4.0 | 0.007 | 8/40 (H4, NCI-H2030, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.722×** | -3.7 | 0.021 | 14/41 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.718×** | -3.6 | 0.025 | 8/41 (LS 180, SNU-423, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -3.4 | 0.045 | 12/43 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 35.6 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0786× (z -18.6) |
| [[LoVo (line)]] | wt | 20.7 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0507× (z -18.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -11.6) |
| [[H4 (line)]] | wt | 52.0 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0907× (z -9.5) |
| [[COLO 205 (line)]] | alt | 14.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0608× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0747× (z -8.8) |
| [[HOP62 (line)]] | alt | 2.85 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0575× (z -9.1) |
| [[SNU-1 (line)]] | wt | 8.48 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0638× (z -8.7) |
| [[A-172 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02580]] | +0.64 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[UGT1A1]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[GPA33]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[LINC02331]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[TPRXL]] | +0.61 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[MUC12]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PTPRB]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[UGT1A6]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[LINC01559]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[B3GALT5]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TMPRSS3]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[UGT1A9]] | +0.57 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3]] | -0.48 | -0.54 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FCGBP]] | B | FCGBP activity raises AOAH's level | lines that do not express FCGBP (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without FCGBP | 0.060 | ⚠ within organs, on part of the lines; also absent: LCN2, NPNT, RNF183; maybe low, not absent |
| [[CDH17]] | B | CDH17 activity raises AOAH's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 2.21× lower at baseline in the lines without CDH17 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[EHF]] | B | EHF activity raises AOAH's level | lines that do not express EHF (27) vs lines expressing it (23) | 1.66× lower at baseline in the lines without EHF | 0.090 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Futibatinib (drug)]] 5 µM | C | AOAH activity lowers the cells' numbers under Futibatinib 5 µM (makes them more sensitive) | lines that do not express AOAH (3) vs lines expressing it (45) | the lines without AOAH: 1.45× the cells of the other lines | 0.078 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; co-occurs with RB1; also absent: TNFAIP3, KIFC3, CAMK2D; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, 50.6); signed map (64.4, 3.9). **Vector** length 61.1, 9.17% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.58 to 4); *Aspirin ADME* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +2.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -4.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | acyloxyacyl hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.2 — chr7:36,512,941-36,724,549 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Saposin B type domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P28039](https://www.uniprot.org/uniprotkb/P28039) (Acyloxyacyl hydrolase):

> Removes the secondary (acyloxyacyl-linked) fatty acyl chains from the lipid A region of bacterial lipopolysaccharides. By breaking down LPS, terminates the host response to bacterial infection and prevents prolonged and damaging inflammatory responses (By similarity). In peritoneal macrophages, seems to be important for recovery from a state of immune tolerance following infection by Gram-negative bacteria (By similarity).

**Summary**, from NCBI Gene [313](https://www.ncbi.nlm.nih.gov/gene/313):

> This locus encodes both the light and heavy subunits of acyloxyacyl hydrolase. The encoded enzyme catalyzes the hydrolysis of acyloxylacyl-linked fatty acyl chains from bacterial lipopolysaccharides, effectively detoxifying these molecules. The encoded protein may play a role in modulating host inflammatory response to gram-negative bacteria. Alternatively spliced transcript variants have been described.[provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:548) · Entrez [313](https://www.ncbi.nlm.nih.gov/gene/313) · UniProt [P28039](https://www.uniprot.org/uniprotkb/P28039) · Ensembl [ENSG00000136250](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136250)

## Data

Gene col 5844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5844); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5844]; `tensor/DDL_lfc|DDL_z.npy` [5844]; `embed/gene_vectors.npy` [5844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5844 or target_col == 5844). Every well: [[AOAH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AOAH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
