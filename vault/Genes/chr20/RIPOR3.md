---
symbol: "RIPOR3"
type: "gene"
col: 481
ensembl_id: "ENSG00000042062"
name: "RIPOR family member 3"
location: "20q13.13"
module: 21
arm: "+"
pooled_cpm: 6.2
n_lines_expressing: 45
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# RIPOR3

*RIPOR family member 3* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.91× (z +16.3, q 0e+00, up in 26 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0904×; ⚠ cell-cycle shift, explains ~13% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (PANC-1 0.172×); [[Orlistat (drug)]] 0.05 µM in 1 line (AsPC-1 0.0780×); [[Cyclosporin A (drug)]] 5 µM in 1 line (HT-29 0.0517×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP2]] (+0.64, fdr 7e-06), [[MIR4300HG]] (+0.64, fdr 7e-06), [[GRIA1]] (+0.64, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TTN]] → it (grade C ⚠); 2 go from it, the strongest it → [[PAPLN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.91×** | +16.3 | 0e+00 | 26/32 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +12.1 | 2e-31 | 9/18 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +12.0 | 7e-31 | 22/34 (J82, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +10.6 | 4e-24 | 3/7 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +9.4 | 5e-19 | 24/41 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +8.3 | 7e-15 | 5/9 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +6.4 | 1e-08 | 13/40 (J82, NCI-H23, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +6.2 | 4e-08 | 17/41 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +5.9 | 3e-07 | 14/38 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +5.6 | 1e-06 | 1/15 (HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.3 | 8e-04 | 5/41 (NCI-H2030, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +4.3 | 1e-03 | 11/37 (J82, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.002 | 9/37 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.002 | 8/34 (BT-474, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.004 | 4/27 (A-427, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.014 | 7/37 (SW480, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.030 | 2/37 (SW 900, KATO III) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.032 | 4/38 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.053 | 1/28 (HEC-1-A) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0904×; ⚠ cell-cycle shift, explains ~13% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (PANC-1 0.172×); [[Orlistat (drug)]] 0.05 µM in 1 line (AsPC-1 0.0780×); [[Cyclosporin A (drug)]] 5 µM in 1 line (HT-29 0.0517×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 40.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -10.3) |
| [[A-427 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0904× (z -11.0) ⚠ cell-cycle shift, explains ~13% of this change |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0780× (z -9.6) |
| [[BT-474 (line)]] | alt | 8.23 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.25× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 2.39 | 0 | 1 | — | [[Cyclosporin A (drug)]] 5 µM 0.0517× (z -8.5) |
| [[J82 (line)]] | alt | 4.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +9.9) | — |
| [[KATO III (line)]] | alt | 2.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +9.1) | — |
| [[A-172 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[GRIA1]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[RBFOX3]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[STARD13-AS]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SEC1P]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[LINC02755]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ASIC2]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[MYO16]] | +0.60 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[KCNIP1]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[MAP3K20-AS1]] | +0.59 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTN]] | C | TTN activity lowers RIPOR3's level | lines that do not express TTN (4) vs lines expressing it (46) | 2.65× higher at baseline in the lines without TTN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZSWIM5; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPLN]] | B | RIPOR3 activity raises PAPLN's level | lines that do not express RIPOR3 (5) vs lines expressing it (45) | 2.50× lower at baseline in the lines without RIPOR3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SYNPO2, PER3, ENSG00000274265; maybe low, not absent |
| [[BMAL2-AS1]] | B | RIPOR3 activity raises BMAL2-AS1's level | lines that do not express RIPOR3 (5) vs lines expressing it (45) | 1.26× lower at baseline in the lines without RIPOR3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SYNPO2, PER3, ENSG00000274265; maybe low, not absent |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.4, 30.5); signed map (30.7, 15.5). **Vector** length 42.2, 4.64% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RIPOR family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,586,108-50,691,542 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ530I15.2, dJ530I15.3; previously C20orf175, C20orf176, FAM65C |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q96MK2](https://www.uniprot.org/uniprotkb/Q96MK2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:16168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16168) · Entrez [140876](https://www.ncbi.nlm.nih.gov/gene/140876) · UniProt [Q96MK2](https://www.uniprot.org/uniprotkb/Q96MK2) · Ensembl [ENSG00000042062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042062)

## Data

Gene col 481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 481); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 481]; `tensor/DDL_lfc|DDL_z.npy` [481]; `embed/gene_vectors.npy` [481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 481 or target_col == 481). Every well: [[RIPOR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIPOR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
