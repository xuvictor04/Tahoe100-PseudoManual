---
symbol: "CCNL2"
type: "gene"
col: 13325
ensembl_id: "ENSG00000221978"
name: "cyclin L2"
location: "1p36.33"
module: 157
arm: "+"
pooled_cpm: 46.5
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# CCNL2

*cyclin L2* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.97× (z +8.8, q 8e-16, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hydroxyurea (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.286×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LENG8]] (+0.71, fdr 7e-06), [[GOLGA8A]] (+0.68, fdr 7e-06), [[CDK5RAP3]] (+0.67, fdr 1e-05); moves opposite to [[CBR1]] (-0.63, fdr 1e-05), [[SMIM30]] (-0.51, fdr 4e-04), [[TWF2]] (-0.48, fdr 5e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.97×** | +8.8 | 8e-16 | 46/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.2 | 2e-10 | 40/48 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +7.0 | 6e-10 | 41/44 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.3 | 4e-08 | 41/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +5.9 | 3e-07 | 28/40 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 4e-07 | 37/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.9 | 4e-07 | 35/48 (HEC-1-A, RKO, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +5.7 | 1e-06 | 35/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +5.5 | 3e-06 | 29/47 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.9 | 4e-05 | 34/48 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.8 | 9e-05 | 34/49 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.4 | 6e-04 | 2/49 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +4.0 | 0.002 | 29/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +4.0 | 0.002 | 33/48 (Hs 766T, A498, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.018 | 26/48 (SNU-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.045 | 22/47 (LS 180, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.045 | 22/48 (RKO, Hs 766T, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.056 | 20/48 (A-172, BT-474, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hydroxyurea (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.286×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 52.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 41.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 49.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.92× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 65.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +11.0) | — |
| [[A-172 (line)]] | wt | 31.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 46.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.286× (z -8.5) |
| [[KATO III (line)]] | alt | 37.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +9.0) | — |
| [[LoVo (line)]] | wt | 39.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +9.6) | — |
| [[RKO (line)]] | wt | 48.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 50.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.8) | — |
| [[A-427 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LENG8]] | +0.71 | +0.58 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[GOLGA8A]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[CDK5RAP3]] | +0.67 | +0.57 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[AKT2]] | +0.66 | +0.38 / +0.71 | both halves | 7e-05 |  |
| [[AP1G2-AS1]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[EME2]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[INPPL1]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[CTBP1]] | +0.62 | +0.37 / +0.74 | both halves | 7e-05 |  |
| [[ARGLU1]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CLPTM1L]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SNHG22]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[DMWD]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBR1]] | -0.63 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[SMIM30]] | -0.51 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[TWF2]] | -0.48 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[GSKIP]] | -0.48 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ISCA2]] | -0.48 | -0.20 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[MRPL17]] | -0.47 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCNL2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.3, -24.8); signed map (4.1, -5.3). **Vector** length 108, 28.3% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.8 | +1.4 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +2.6 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -0.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cyclin L2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,385,711-1,399,335 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ania-6b, PCEE, SB138, HLA-ISO, CCNS; previously CCNM |
| Gene groups (HGNC) | Cyclins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S94](https://www.uniprot.org/uniprotkb/Q96S94) (Cyclin-L2):

> Regulatory component of the cyclin-L-CDK11 complex that regulates transcription and pre-mRNA splicing.

**Summary**, from NCBI Gene [81669](https://www.ncbi.nlm.nih.gov/gene/81669):

> The protein encoded by this gene belongs to the cyclin family. Through its interaction with several proteins, such as RNA polymerase II, splicing factors, and cyclin-dependent kinases, this protein functions as a regulator of the pre-mRNA splicing process, as well as in inducing apoptosis by modulating the expression of apoptotic and antiapoptotic proteins. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:20570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20570) · Entrez [81669](https://www.ncbi.nlm.nih.gov/gene/81669) · UniProt [Q96S94](https://www.uniprot.org/uniprotkb/Q96S94) · Ensembl [ENSG00000221978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221978)

## Data

Gene col 13325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13325); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13325]; `tensor/DDL_lfc|DDL_z.npy` [13325]; `embed/gene_vectors.npy` [13325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13325 or target_col == 13325). Every well: [[CCNL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
