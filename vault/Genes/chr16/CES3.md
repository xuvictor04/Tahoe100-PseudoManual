---
symbol: "CES3"
type: "gene"
col: 10302
ensembl_id: "ENSG00000172828"
name: "carboxylesterase 3"
location: "16q22.1"
module: 35
arm: "+"
pooled_cpm: 2.17
n_lines_expressing: 40
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# CES3

*carboxylesterase 3* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +9.7, q 2e-19, up in 10 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.577× (z -4.8, q 8e-04, down in 15 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (CFPAC-1 0.0469×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymopentin (drug)]] 5 µM in 1 line (SW480 0.0550×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A498 0.0543×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPEAR]] (+0.69, fdr 7e-06), [[NAPA-AS1]] (+0.66, fdr 1e-05), [[SPATA18]] (+0.65, fdr 1e-05); moves opposite to [[NAPG]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ITFG2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +9.7 | 2e-19 | 10/21 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.11×** | +9.5 | 4e-19 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +9.3 | 4e-18 | 11/21 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +6.7 | 2e-09 | 2/5 (HEC-1-A, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +6.2 | 7e-08 | 3/6 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +6.2 | 7e-08 | 9/22 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +4.8 | 1e-04 | 6/33 (LS 180, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +4.7 | 2e-04 | 8/34 (KATO III, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.6 | 2e-04 | 1/9 (LS 180) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.3 | 0.001 | 5/18 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.7 | 0.011 | 4/12 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.013 | 6/26 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.016 | 1/16 (CFPAC-1) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.2 | 0.052 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.44×** | +3.1 | 0.057 | 3/22 (SW48, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.057 | 5/19 (LS 180, HEC-1-A, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.0 | 0.073 | 1/13 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.073 | 8/27 (CFPAC-1, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10302.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (CFPAC-1 0.0469×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymopentin (drug)]] 5 µM in 1 line (SW480 0.0550×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A498 0.0543×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -4.8 | 8e-04 | 15/30 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.698× | -3.2 | 0.44 | 4/34 (NCI-H2030, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.32 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0543× (z -8.5) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 4.51 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0469× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 1.47 | 0 | 1 | — | [[Thymopentin (drug)]] 5 µM 0.0550× (z -9.0) |
| [[A-172 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.692 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.428 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.694 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.590 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.757 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.614 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.580 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.630 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.658 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPEAR]] | +0.69 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[NAPA-AS1]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SPATA18]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[AJUBA-DT]] | +0.65 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[BANK1]] | +0.65 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[TAPBPL]] | +0.64 | +0.69 / +0.38 | both halves | 7e-05 |  |
| [[NEIL1]] | +0.63 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[GUCY2C-AS1]] | +0.61 | +0.71 / +0.33 | both halves | 1e-04 |  |
| [[ARL14EP-DT]] | +0.61 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[DLL1]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZC2HC1C]] | +0.59 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[FCGRT]] | +0.59 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPG]] | -0.54 | -0.62 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITFG2-AS1]] | B | CES3 activity raises ITFG2-AS1's level | lines that do not express CES3 (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without CES3 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000288075; maybe low, not absent |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.560). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.0, 25.4); signed map (37.0, -5.5). **Vector** length 37.0, 4.67% of its response variance represented; |z| ≥ 3 in 787 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.1 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | +1.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.8 | -0.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | carboxylesterase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:66,961,245-66,975,149 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21736, ES31 |
| Gene groups (HGNC) | Carboxylesterases |
| Reactome | 6 pathways, smallest: LDL clearance; Plasma lipoprotein clearance; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWW8](https://www.uniprot.org/uniprotkb/Q6UWW8) (Carboxylesterase 3):

> Involved in the detoxification of xenobiotics and in the activation of ester and amide prodrugs. Shows low catalytic efficiency for hydrolysis of CPT-11 (7-ethyl-10-[4-(1-piperidino)-1-piperidino]-carbonyloxycamptothecin), a prodrug for camptothecin used in cancer therapeutics.

**Summary**, from NCBI Gene [23491](https://www.ncbi.nlm.nih.gov/gene/23491):

> This gene encodes a member of the carboxylesterase large family. The family members are responsible for the hydrolysis or transesterification of various xenobiotics, such as cocaine and heroin, and endogenous substrates with ester, thioester, or amide bonds. They may participate in fatty acyl and cholesterol ester metabolism, and may play a role in the blood-brain barrier system. This gene is expressed in several tissues, particularly in colon, trachea and in brain, and the protein participates …

**Accessions** — [HGNC:1865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1865) · Entrez [23491](https://www.ncbi.nlm.nih.gov/gene/23491) · UniProt [Q6UWW8](https://www.uniprot.org/uniprotkb/Q6UWW8) · Ensembl [ENSG00000172828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172828)

## Data

Gene col 10302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10302); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10302]; `tensor/DDL_lfc|DDL_z.npy` [10302]; `embed/gene_vectors.npy` [10302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10302 or target_col == 10302). Every well: [[CES3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CES3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
