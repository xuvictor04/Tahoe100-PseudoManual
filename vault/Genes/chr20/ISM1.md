---
symbol: "ISM1"
type: "gene"
col: 2101
ensembl_id: "ENSG00000101230"
name: "isthmin 1"
location: "20p12.1"
module: 61
arm: "+"
pooled_cpm: 2.6
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# ISM1

*isthmin 1* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.61× (z +11.8, q 2e-29, up in 7 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.32× (z +11.0, q 1e-25, up in 13 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.238×, HepG2/C3A 0.210×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW480 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (SW 900 0.113×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL3RA]] (+0.63, fdr 1e-05), [[ADAMTS19]] (+0.63, fdr 1e-05), [[CACNA1E]] (+0.62, fdr 1e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RGL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.61×** | +11.8 | 2e-29 | 7/12 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.72×** | +11.6 | 1e-28 | 2/5 (A498, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +11.0 | 1e-25 | 13/27 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +8.2 | 3e-14 | 3/6 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +7.9 | 3e-13 | 20/41 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.92×** | +6.0 | 2e-07 | 13/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.76×** | +5.2 | 2e-05 | 11/42 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.2 | 2e-05 | 2/12 (HS-578T, LoVo) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.0 | 4e-05 | 6/41 (A549, RPMI-7951, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.72×** | +4.8 | 9e-05 | 7/30 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.7 | 2e-04 | 3/15 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +4.6 | 2e-04 | 10/44 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.6 | 2e-04 | 11/33 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.63×** | +4.5 | 3e-04 | 12/39 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +4.3 | 7e-04 | 8/28 (CFPAC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.067 | 1/18 (SW480) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.072 | 0/42 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2101.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW480 0.238×, HepG2/C3A 0.210×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW480 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.5 µM in 1 line (SW 900 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -4.3 | 0.011 | 14/45 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.708× | -3.2 | 0.40 | 7/36 (HOP62, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.26 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +11.9) | — |
| [[SW480 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.4) |
| [[A549 (line)]] | wt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -9.0) |
| [[SW 900 (line)]] | alt | 9.76 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.113× (z -9.3) |
| [[A-172 (line)]] | wt | 0.868 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.712 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.880 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.856 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.956 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.718 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.871 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL3RA]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ADAMTS19]] | +0.63 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CACNA1E]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[TMEM163]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SYN1]] | +0.60 | +0.46 / +0.71 | both halves | 2e-05 |  |
| [[CELF5]] | +0.60 | +0.37 / +0.68 | both halves | 9e-05 |  |
| [[DKK2]] | +0.59 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[MTUS2]] | +0.59 | +0.31 / +0.69 | both halves | 2e-04 |  |
| [[VSIG1]] | +0.58 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[GSG1L]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[OPCML]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[DACH2]] | +0.56 | +0.46 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ISM1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC24A3]] | B | SLC24A3 activity raises ISM1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.59× lower at baseline in the lines without SLC24A3 | 0.049 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[IL19]] | B | IL19 activity raises ISM1's level | lines that do not express IL19 (23) vs lines expressing it (27) | 1.45× lower at baseline in the lines without IL19 | 0.065 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGL1]] | C | ISM1's natural level weakens RGL1's drug response | ISM1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.55; direction not clear | 0.096 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, 35.7); signed map (31.2, 18.7). **Vector** length 41.3, 4.63% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +0.9 | +1.5 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | isthmin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:13,221,274-13,300,651 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA149I18.1; previously C20orf82 |
| Gene groups (HGNC) | Isthmin family |
| Matched by | ensembl_id |

**Function**, from UniProt [B1AKI9](https://www.uniprot.org/uniprotkb/B1AKI9) (Isthmin-1):

> Acts as an angiogenesis inhibitor.

**Summary**, from NCBI Gene [140862](https://www.ncbi.nlm.nih.gov/gene/140862):

> Predicted to be involved in negative regulation of angiogenesis. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16213) · Entrez [140862](https://www.ncbi.nlm.nih.gov/gene/140862) · UniProt [B1AKI9](https://www.uniprot.org/uniprotkb/B1AKI9) · Ensembl [ENSG00000101230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101230)

## Data

Gene col 2101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2101); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2101]; `tensor/DDL_lfc|DDL_z.npy` [2101]; `embed/gene_vectors.npy` [2101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2101 or target_col == 2101). Every well: [[ISM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
