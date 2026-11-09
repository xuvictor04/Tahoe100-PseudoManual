---
symbol: "NPPB"
type: "gene"
col: 4239
ensembl_id: "ENSG00000120937"
name: "natriuretic peptide B"
location: "1p36.22"
module: 180
arm: "+"
pooled_cpm: 3.03
n_lines_expressing: 6
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# NPPB

*natriuretic peptide B* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 11.9× (z +9.1, q 7e-17, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.13× (z +4.2, q 0.002, up in 0 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (J82 0.102×); [[Selinexor (drug)]] 0.5 µM in 1 line (J82 0.124×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPA4]] (+0.56, fdr 2e-05), [[CCDC124]] (+0.49, fdr 1e-04), [[PSG5]] (+0.47, fdr 4e-04); moves opposite to [[JCAD]] (-0.44, fdr 6e-05), [[PTPDC1]] (-0.42, fdr 1e-04), [[NHSL1]] (-0.40, fdr 3e-04).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SIM1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 13 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.9×** | +9.1 | 7e-17 | 1/1 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.35×** | +8.8 | 4e-16 | 1/1 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.27×** | +6.7 | 5e-09 | 1/1 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.22×** | +4.6 | 6e-04 | 1/2 (J82) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +4.5 | 6e-04 | 2/2 (J82, A-172) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.26×** | +4.5 | 6e-04 | 1/3 (A-172) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.37×** | +4.4 | 7e-04 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.07×** | +4.4 | 8e-04 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.13×** | +4.2 | 0.002 | 0/4 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **2.65×** | +3.8 | 0.008 | 0/2 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.68×** | +3.6 | 0.016 | 0/2 | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.51×** | +3.6 | 0.016 | 0/2 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.10×** | +3.3 | 0.033 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +3.3 | 0.033 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.33×** | +3.3 | 0.035 | 0/2 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4239.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (J82 0.102×); [[Selinexor (drug)]] 0.5 µM in 1 line (J82 0.124×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.413× | -3.5 | 0.23 | 1/4 (J82) | inconsistent across doses |  |
| [[Dabrafenib (drug)]] 5 µM |  | 0.234× | -3.0 | 0.62 | 1/4 (J82) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.102× (z -13.2) |
| [[A-172 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.132 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.138 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.208 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.133 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.175 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.192 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.158 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.144 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.926 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.138 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.197 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.144 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.162 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.145 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.158 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.130 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.151 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.134 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.190 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.161 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.167 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.159 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.143 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.178 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.168 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.181 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.622 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPA4]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[CCDC124]] | +0.49 | +0.36 / +0.36 | both halves | 1e-04 |  |
| [[PSG5]] | +0.47 | +0.26 / +0.53 | both halves | 4e-04 |  |
| [[TMEM40]] | +0.46 | +0.38 / +0.29 | both halves | 3e-04 |  |
| [[PPP2R5B]] | +0.45 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[SYTL2]] | +0.44 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[ALPK2]] | +0.44 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[PTPRF]] | +0.44 | +0.27 / +0.47 | both halves | 3e-04 |  |
| [[CCDC80]] | +0.44 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[LIMCH1]] | +0.44 | +0.31 / +0.38 | both halves | 2e-04 |  |
| [[DTNA]] | +0.43 | +0.37 / +0.41 | both halves | 9e-05 |  |
| [[ADAMTS16]] | +0.43 | +0.40 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JCAD]] | -0.44 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[PTPDC1]] | -0.42 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[NHSL1]] | -0.40 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[GNG12-AS1]] | -0.38 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[RESF1]] | -0.38 | -0.27 / -0.33 | both halves | 3e-04 |  |
| [[SOCS6]] | -0.38 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[RNF14]] | -0.36 | -0.35 / -0.24 | both halves | 5e-04 |  |
| [[SPRY4-AS1]] | -0.36 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[NIPAL2]] | -0.35 | -0.26 / -0.25 | both halves | 4e-04 |  |
| [[PALB2]] | -0.35 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[SH3RF3]] | -0.35 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIM1]] | C | SIM1 activity raises NPPB's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.30× lower at baseline in the lines without SIM1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[PSG5]] | C | PSG5 activity raises NPPB's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 2.05× lower at baseline in the lines without PSG5 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[MARCOL]] | C | MARCOL activity raises NPPB's level | lines that do not express MARCOL (45) vs lines expressing it (5) | 1.49× lower at baseline in the lines without MARCOL | 0.059 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises NPPB's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 2.07× lower at baseline in the lines without PSG4 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[RB1]] | C | RB1 activity lowers NPPB's level | recorded loss-of-function mutation of RB1 in 3 lines vs 46 not recorded | 6.83× higher at baseline in the RB1-altered lines | 0.328 over the table, 0.067 within its group | ⚠ within its group only (a lead); few lines (3 vs 46); tissue-confounded; across organs |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.367). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.5, 18.2); signed map (29.9, 31.2). **Vector** length 12.5, 4.79% of its response variance represented; |z| ≥ 3 in 82 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +0.6 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.5 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.5 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.5 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.5 | +1.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -0.8 | +4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.6 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.4 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.3 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -0.3 | +0.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.3 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | natriuretic peptide B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,857,464-11,858,945 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Natriuretic peptides |
| Matched by | ensembl_id |

**Function**, from UniProt [P16860](https://www.uniprot.org/uniprotkb/P16860) (Natriuretic peptides B):

> [Brain natriuretic peptide 32]: Cardiac hormone that plays a key role in mediating cardio-renal homeostasis. May also function as a paracrine antifibrotic factor in the heart (By similarity). Acts by specifically binding and stimulating NPR1 to produce cGMP, which in turn activates effector proteins that drive various biological responses. Involved in regulating the extracellular fluid volume and maintaining the fluid-electrolyte balance through natriuresis, diuresis, vasorelaxation, and …

**Summary**, from NCBI Gene [4879](https://www.ncbi.nlm.nih.gov/gene/4879):

> This gene is a member of the natriuretic peptide family and encodes a secreted protein which functions as a cardiac hormone. The protein undergoes two cleavage events, one within the cell and a second after secretion into the blood. The protein's biological actions include natriuresis, diuresis, vasorelaxation, inhibition of renin and aldosterone secretion, and a key role in cardiovascular homeostasis. A high concentration of this protein in the bloodstream is indicative of heart failure. The …

**Accessions** — [HGNC:7940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7940) · Entrez [4879](https://www.ncbi.nlm.nih.gov/gene/4879) · UniProt [P16860](https://www.uniprot.org/uniprotkb/P16860) · Ensembl [ENSG00000120937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120937)

## Data

Gene col 4239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4239); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4239]; `tensor/DDL_lfc|DDL_z.npy` [4239]; `embed/gene_vectors.npy` [4239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4239 or target_col == 4239). Every well: [[NPPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
