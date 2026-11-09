---
symbol: "G2E3-AS1"
type: "gene"
col: 15054
ensembl_id: "ENSG00000257636"
name: "G2E3 antisense RNA 1"
location: "14q12"
module: 90
arm: "+"
pooled_cpm: 4.17
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# G2E3-AS1

*G2E3 antisense RNA 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.32× (z +15.6, q 0e+00, up in 32 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ritonavir (drug)]] 0.5 µM in 1 line (PANC-1 0.0766×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00861]] (+0.84, fdr 7e-06), [[GRM7]] (+0.82, fdr 7e-06), [[CNTNAP5]] (+0.79, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC00491]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.32×** | +15.6 | 0e+00 | 32/36 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +12.7 | 3e-34 | 27/36 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +10.2 | 2e-22 | 4/7 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +9.8 | 1e-20 | 13/19 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +8.4 | 3e-15 | 7/10 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.24×** | +7.4 | 1e-11 | 20/34 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.95×** | +6.1 | 6e-08 | 18/43 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +5.2 | 1e-05 | 10/32 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +5.0 | 4e-05 | 15/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.9 | 7e-05 | 9/25 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.8 | 1e-04 | 11/46 (PANC-1, A549, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.65×** | +4.6 | 2e-04 | 6/19 (A498, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.53×** | +4.5 | 4e-04 | 0/8 | top dose only | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.001 | 5/32 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.60×** | +4.1 | 0.001 | 14/41 (AsPC-1, MIA PaCa-2, …) | top dose only | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.002 | 8/35 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +4.0 | 0.002 | 12/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Cepharanthine (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.009 | 4/35 (SHP-77, KATO III, …) | two highest doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.017 | 4/45 (SNU-423, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.022 | 7/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.041 | 3/36 (SK-MEL-2, LoVo, …) | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.075 | 7/39 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15054.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ritonavir (drug)]] 0.5 µM in 1 line (PANC-1 0.0766×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.864× | -5.0 | 4e-04 | 23/47 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.693× | -3.4 | 0.20 | 4/46 (HCT15, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.37 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 13.4× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.50× (z +9.3) | [[Ritonavir (drug)]] 0.5 µM 0.0766× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 2.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +10.5) | — |
| [[A549 (line)]] | wt | 2.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.61× (z +8.5) | — |
| [[A-172 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00861]] | +0.84 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[GRM7]] | +0.82 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.79 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.78 | +0.62 / +0.76 | both halves | 7e-06 | same gene group |
| [[C2CD5-AS1]] | +0.78 | +0.62 / +0.77 | both halves | 7e-06 | same gene group |
| [[SPATA21]] | +0.78 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.77 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.77 | +0.69 / +0.72 | both halves | 7e-06 | same gene group |
| [[DLEU7]] | +0.76 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.76 | +0.63 / +0.74 | both halves | 7e-06 | same gene group |
| [[PAXBP1-AS1]] | +0.75 | +0.70 / +0.68 | both halves | 7e-06 | same gene group |
| [[SYNM-AS1]] | +0.74 | +0.66 / +0.66 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00491]] | B | LINC00491 activity raises G2E3-AS1's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 1.66× lower at baseline in the lines without LINC00491 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7 |
| [[TOP2A]] | B | TOP2A activity lowers G2E3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OPRD1]] | B | OPRD1 activity raises G2E3-AS1's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.39× lower at baseline in the lines without OPRD1 | 0.075 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[SLCO6A1]] | B | SLCO6A1 activity raises G2E3-AS1's level | lines that do not express SLCO6A1 (20) vs lines expressing it (30) | 1.46× lower at baseline in the lines without SLCO6A1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ZNF883, SOX5, KCNK2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.1, 28.3); signed map (34.3, 12.8). **Vector** length 45.0, 4.99% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -5.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | +3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | G2E3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q12 — chr14:30,437,992-30,573,629 (-) |
| Ensembl biotype | lncRNA |
| Also known as | CAT1647, lincPRKD |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53463) · Entrez [105370431](https://www.ncbi.nlm.nih.gov/gene/105370431) · Ensembl [ENSG00000257636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257636)

## Data

Gene col 15054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15054); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15054]; `tensor/DDL_lfc|DDL_z.npy` [15054]; `embed/gene_vectors.npy` [15054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15054 or target_col == 15054). Every well: [[G2E3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/G2E3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
