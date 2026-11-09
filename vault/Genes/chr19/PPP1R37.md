---
symbol: "PPP1R37"
type: "gene"
col: 2510
ensembl_id: "ENSG00000104866"
name: "protein phosphatase 1 regulatory subunit 37"
location: "19q13.32"
module: 138
arm: "+"
pooled_cpm: 7.97
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# PPP1R37

*protein phosphatase 1 regulatory subunit 37* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.33× (z +17.4, q 0e+00, up in 37 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (A-172 0.0589×); [[DT-061 (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0631×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0864×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2B]] (+0.73, fdr 7e-06), [[CACTIN]] (+0.63, fdr 1e-05), [[BLOC1S3]] (+0.63, fdr 7e-06, ⚠ same locus), [[TAOK2]] (+0.63, fdr 1e-05); moves opposite to [[SNHG30]] (-0.55, fdr 1e-05), [[PPHLN1]] (-0.54, fdr 1e-05), [[GRB2]] (-0.52, fdr 3e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[DXO]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +17.4 | 0e+00 | 37/40 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +10.9 | 2e-25 | 32/41 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +10.4 | 4e-23 | 38/44 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +8.5 | 3e-15 | 30/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +7.0 | 4e-10 | 22/47 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +5.9 | 3e-07 | 17/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 8e-06 | 13/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +5.3 | 1e-05 | 15/39 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 1e-05 | 19/46 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 6e-05 | 12/46 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 2e-04 | 12/45 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.9 | 0.004 | 14/42 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.060 | 3/46 (J82, RPMI-7951, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.060 | 5/46 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.1 | 0.075 | 4/47 (HEC-1-A, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2510.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (A-172 0.0589×); [[DT-061 (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0631×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0864×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.837× | -3.7 | 0.10 | 9/46 (MIA PaCa-2, NCI-H2347, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -3.3 | 0.29 | 9/47 (HOP62, NCI-H2347, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.12 | 0 | 3 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0589× (z -11.6) |
| [[A-427 (line)]] | wt | 5.79 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.101× (z -9.4) ⚠ toxic |
| [[C32 (line)]] | wt | 7.24 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0760× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 6.74 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.127× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0864× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 7.15 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0631× (z -10.4) |
| [[A498 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2B]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CACTIN]] | +0.63 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[BLOC1S3]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 | ⚠ same locus (30.7 kb, same strand: neighbours can correlate without regulation) |
| [[TAOK2]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[GFER]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZNF687]] | +0.62 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[USP19]] | +0.62 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[REPIN1]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CNOT3]] | +0.59 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[ZNF574]] | +0.59 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[LCAT]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[TNKS1BP1]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[UAP1L1]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG30]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[PPHLN1]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[GRB2]] | -0.52 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[ATP2C1]] | -0.52 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[BTAF1]] | -0.52 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[RPL6]] | -0.51 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[PROCR]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[HPRT1]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[TMEM167A]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[SUMO1]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DXO]] | C | PPP1R37's natural level weakens DXO's drug response | PPP1R37's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.18; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.4, -1.8); signed map (1.9, -9.0). **Vector** length 57.2, 7.59% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +17.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +10.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.6 | +5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.0 | +0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,091,396-45,148,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LRRC68 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [O75864](https://www.uniprot.org/uniprotkb/O75864) (Protein phosphatase 1 regulatory subunit 37):

> Inhibits phosphatase activity of protein phosphatase 1 (PP1) complexes.

**Summary**, from NCBI Gene [284352](https://www.ncbi.nlm.nih.gov/gene/284352):

> Predicted to enable protein phosphatase inhibitor activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27607) · Entrez [284352](https://www.ncbi.nlm.nih.gov/gene/284352) · UniProt [O75864](https://www.uniprot.org/uniprotkb/O75864) · Ensembl [ENSG00000104866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104866)

## Data

Gene col 2510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2510); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2510]; `tensor/DDL_lfc|DDL_z.npy` [2510]; `embed/gene_vectors.npy` [2510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2510 or target_col == 2510). Every well: [[PPP1R37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
