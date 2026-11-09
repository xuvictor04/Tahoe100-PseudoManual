---
symbol: "DPYS"
type: "gene"
col: 7208
ensembl_id: "ENSG00000147647"
name: "dihydropyrimidinase"
location: "8q22.3"
module: 39
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 36
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# DPYS

*dihydropyrimidinase* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.82× (z +17.0, q 0e+00, up in 19 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0782×; ⚠ cell-cycle shift, explains ~97% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0796×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARIN1B]] (+0.89, fdr 7e-06), [[USP50]] (+0.86, fdr 7e-06), [[LINC00393]] (+0.83, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[TG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.82×** | +17.0 | 0e+00 | 19/20 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.70×** | +14.2 | 2e-43 | 1/3 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.03×** | +12.3 | 2e-32 | 4/9 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.47×** | +12.0 | 4e-31 | 12/19 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.42×** | +11.8 | 8e-30 | 2/4 (A498, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.99×** | +11.0 | 4e-26 | 17/23 (C32, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.21×** | +8.0 | 1e-13 | 10/16 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +7.2 | 5e-11 | 11/17 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.29×** | +5.6 | 1e-06 | 17/30 (A498, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +5.6 | 1e-06 | 6/27 (NCI-H2347, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.4 | 3e-06 | 6/27 (A498, NCI-H2347, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.29×** | +5.3 | 5e-06 | 11/25 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +5.1 | 1e-05 | 3/11 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +4.1 | 0.002 | 7/23 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.003 | 3/27 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +3.9 | 0.004 | 2/26 (HOP62, A498) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.67×** | +3.5 | 0.014 | 2/12 (HEC-1-A, RPMI-7951) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.022 | 1/17 (NCI-H1792) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.024 | 8/25 (A498, RKO, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7208.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0782×; ⚠ cell-cycle shift, explains ~97% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0796×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | 0.362× | -3.7 | 0.14 | 8/14 (J82, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.05 µM |  | 0.584× | -3.4 | 0.15 | 7/26 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.712× | -3.3 | 0.15 | 9/26 (C32, C-33 A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.646× | -3.0 | 0.34 | 9/22 (C32, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 8.92 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0782× (z -8.5) ⚠ cell-cycle shift, explains ~97% of this change |
| [[A-172 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.543 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.928 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.724 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.532 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.620 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.648 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.570 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.587 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.362 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARIN1B]] | +0.89 | +0.87 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[USP50]] | +0.86 | +0.83 / +0.82 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.83 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.83 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.83 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[MPP4]] | +0.83 | +0.82 / +0.80 | both halves | 7e-06 |  |
| [[XG]] | +0.83 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.81 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.80 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.80 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPYS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TG]] | B | DPYS activity raises TG's level | lines that do not express DPYS (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without DPYS | 0.042 | ⚠ within organs, on part of the lines; also absent: SYNE1, ANGPT1, PCDH9; maybe low, not absent |
| [[FSIP1]] | B | DPYS activity raises FSIP1's level | lines that do not express DPYS (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without DPYS | 0.084 | ⚠ within organs, on part of the lines; also absent: SYNE1, ANGPT1, PCDH9; maybe low, not absent |
| [[PHEX]] | B | DPYS activity raises PHEX's level | lines that do not express DPYS (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without DPYS | 0.090 | ⚠ within organs, on part of the lines; also absent: SYNE1, ANGPT1, PCDH9; maybe low, not absent |
| [[LINC01393]] | C | DPYS activity raises LINC01393's level | lines that do not express DPYS (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without DPYS | 0.027 | ⚠ within organs, on part of the lines; also absent: SYNE1, ANGPT1, PCDH9; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.865). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.0, -13.1); signed map (19.1, 9.3). **Vector** length 49.1, 8.93% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +17.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.0 |
| fall | [[Radotinib (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | dihydropyrimidinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:104,330,324-104,467,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DHPase |
| Gene groups (HGNC) | M38 metallopeptidases |
| Reactome | 3 pathways, smallest: Pyrimidine catabolism; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14117](https://www.uniprot.org/uniprotkb/Q14117) (Dihydropyrimidinase):

> Hydrolase that catalyzes the reversible hydrolytic ring opening of 5,6-dihydrouracil and 5,6-dihydrothymine, the second step in the reductive catabolic pathway of uracil and thymine degradation.

**Summary**, from NCBI Gene [1807](https://www.ncbi.nlm.nih.gov/gene/1807):

> Dihydropyrimidinase catalyzes the conversion of 5,6-dihydrouracil to 3-ureidopropionate in pyrimidine metabolism. Dihydropyrimidinase is expressed at a high level in liver and kidney as a major 2.5-kb transcript and a minor 3.8-kb transcript. Defects in the DPYS gene are linked to dihydropyrimidinuria. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3013) · Entrez [1807](https://www.ncbi.nlm.nih.gov/gene/1807) · UniProt [Q14117](https://www.uniprot.org/uniprotkb/Q14117) · Ensembl [ENSG00000147647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147647)

## Data

Gene col 7208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7208); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7208]; `tensor/DDL_lfc|DDL_z.npy` [7208]; `embed/gene_vectors.npy` [7208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7208 or target_col == 7208). Every well: [[DPYS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPYS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
