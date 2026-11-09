---
symbol: "OBI1-AS1"
type: "gene"
col: 13953
ensembl_id: "ENSG00000234377"
name: "OBI1 antisense RNA 1"
location: "13q22.3-q31.1"
module: 166
arm: "+"
pooled_cpm: 2.64
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# OBI1-AS1

*OBI1 antisense RNA 1* — 13q22.3-q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.91× (z +20.3, q 0e+00, up in 24 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.5 µM in 1 line (J82 0.0600×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HPSE2]] (+0.88, fdr 7e-06), [[ESR1]] (+0.85, fdr 7e-06), [[DCC]] (+0.84, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[IHO1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.91×** | +20.3 | 0e+00 | 24/26 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +9.8 | 3e-20 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.90×** | +9.6 | 2e-19 | 29/40 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +9.6 | 2e-19 | 8/12 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.84×** | +9.4 | 7e-19 | 22/35 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +9.0 | 3e-17 | 20/32 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +6.6 | 3e-09 | 15/33 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.3 | 2e-08 | 15/43 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +6.1 | 5e-08 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.3 | 9e-06 | 10/24 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.87×** | +4.0 | 0.003 | 1/6 (HEC-1-A) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.004 | 4/42 (HEC-1-A, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.011 | 3/44 (SW480, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.011 | 8/30 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +3.5 | 0.017 | 1/6 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.027 | 8/34 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.062 | 3/26 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.075 | 3/42 (NCI-H2030, SK-MEL-2, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.093 | 4/38 (J82, COLO 205, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.5 µM in 1 line (J82 0.0600×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 1.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 2.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +8.7) | — |
| [[J82 (line)]] | alt | 2.86 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0600× (z -8.8) |
| [[LoVo (line)]] | wt | 1.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.82× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 1.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.19× (z +8.8) | — |
| [[SW480 (line)]] | alt | 1.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +12.0) | — |
| [[A-172 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPSE2]] | +0.88 | +0.78 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[ESR1]] | +0.85 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[DCC]] | +0.84 | +0.71 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[SORCS1]] | +0.83 | +0.76 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[PKP4-AS1]] | +0.79 | +0.71 / +0.78 | both halves | 7e-06 | same gene group |
| [[CFAP20DC-DT]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.75 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[ST8SIA1]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[CNTN4]] | +0.74 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[LINC00276]] | +0.73 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[USH2A]] | +0.72 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.72 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IHO1]] | B | IHO1 activity raises OBI1-AS1's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 1.67× lower at baseline in the lines without IHO1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers OBI1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL19A1]] | B | COL19A1 activity raises OBI1-AS1's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 1.75× lower at baseline in the lines without COL19A1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7 |
| [[VENTXP1]] | B | VENTXP1 activity raises OBI1-AS1's level | lines that do not express VENTXP1 (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without VENTXP1 | 0.072 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, SLCO6A1; maybe low, not absent |
| [[LHFPL3-AS1]] | B | LHFPL3-AS1 activity raises OBI1-AS1's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 2.62× lower at baseline in the lines without LHFPL3-AS1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1 |
| [[FCRLA]] | B | FCRLA activity raises OBI1-AS1's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 2.11× lower at baseline in the lines without FCRLA | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474 |
| [[LINC02240]] | B | LINC02240 activity raises OBI1-AS1's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 1.72× lower at baseline in the lines without LINC02240 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.895). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.5, 28.0); signed map (32.0, 15.0). **Vector** length 50.0, 6.66% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +20.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | OBI1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q22.3-q31.1 — chr13:77,919,689-78,617,328 (+) |
| Ensembl biotype | lncRNA |
| Also known as | uc.354; previously POU4F1-AS1, RNF219-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42700) · Entrez [100874222](https://www.ncbi.nlm.nih.gov/gene/100874222) · Ensembl [ENSG00000234377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234377)

## Data

Gene col 13953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13953); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13953]; `tensor/DDL_lfc|DDL_z.npy` [13953]; `embed/gene_vectors.npy` [13953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13953 or target_col == 13953). Every well: [[OBI1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OBI1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
