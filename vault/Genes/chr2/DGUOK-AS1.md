---
symbol: "DGUOK-AS1"
type: "gene"
col: 14157
ensembl_id: "ENSG00000237883"
name: "DGUOK antisense RNA 1"
location: "2p13.1"
module: 150
arm: "+"
pooled_cpm: 4.97
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# DGUOK-AS1

*DGUOK antisense RNA 1* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.56× (z +20.5, q 0e+00, up in 37 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0550×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TP53TG5]] (+0.68, fdr 7e-06), [[HEATR4]] (+0.66, fdr 1e-05), [[TRPM2]] (+0.64, fdr 1e-05); moves opposite to [[ALAD]] (-0.56, fdr 2e-04), [[NAA40]] (-0.55, fdr 9e-05), [[ECHS1]] (-0.55, fdr 3e-04).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.56×** | +20.5 | 0e+00 | 37/37 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +11.3 | 4e-27 | 19/38 (NCI-H2030, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +7.3 | 4e-11 | 3/10 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +6.9 | 9e-10 | 22/45 (HS-578T, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +6.6 | 4e-09 | 19/33 (NCI-H460, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.5 | 7e-09 | 8/23 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +6.3 | 2e-08 | 16/44 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +5.4 | 5e-06 | 3/14 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.1 | 2e-05 | 11/35 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.7 | 1e-04 | 10/45 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.8 | 0.008 | 2/28 (NCI-H23, BT-474) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.36×** | +3.6 | 0.016 | 8/36 (COLO 205, NCI-H2030, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.016 | 1/34 (A-427) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.4 | 0.023 | 6/36 (PANC-1, RKO, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.023 | 2/45 (HepG2/C3A, LOX-IMVI) | top dose only |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.032 | 6/33 (HT-29, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.049 | 3/39 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.050 | 4/42 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.050 | 9/46 (NCI-H1792, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14157.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (COLO 205 0.0550×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.737× | -3.5 | 0.12 | 14/46 (HOP62, HT-29, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.728× | -3.5 | 0.12 | 8/43 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.4 | 0.12 | 8/47 (A-172, SHP-77, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.756× | -3.2 | 0.21 | 11/46 (A-427, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.95× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 8.01 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0550× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 9.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +8.7) | — |
| [[LoVo (line)]] | wt | 3.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 3.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 5.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.50× (z +11.0) | — |
| [[A-172 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53TG5]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[HEATR4]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TRPM2]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PJVK]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[LRRC8C-DT]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SORCS3]] | +0.62 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[CASC11]] | +0.61 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[SLC7A7]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SOCS3-DT]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[IL34]] | +0.60 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[OPCML]] | +0.60 | +0.44 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.56 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[NAA40]] | -0.55 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[ECHS1]] | -0.55 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[PHF6]] | -0.54 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[GDE1]] | -0.53 | -0.33 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DGUOK-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.6, 22.8); signed map (29.9, 1.9). **Vector** length 59.0, 8.24% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +20.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -1.8 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | DGUOK antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p13.1 — chr2:73,947,322-73,982,173 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43441) · Entrez [100874048](https://www.ncbi.nlm.nih.gov/gene/100874048) · Ensembl [ENSG00000237883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237883)

## Data

Gene col 14157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14157); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14157]; `tensor/DDL_lfc|DDL_z.npy` [14157]; `embed/gene_vectors.npy` [14157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14157 or target_col == 14157). Every well: [[DGUOK-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGUOK-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
