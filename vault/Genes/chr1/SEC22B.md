---
symbol: "SEC22B"
type: "gene"
col: 15467
ensembl_id: "ENSG00000265808"
name: "SEC22 homolog B, vesicle trafficking protein"
location: "1p12"
module: 56
arm: "+"
pooled_cpm: 63.84
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SEC22B

*SEC22 homolog B, vesicle trafficking protein* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.59× (z +6.4, q 6e-08, up in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (LOX-IMVI 2.92×, Panc 03.27 2.67×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.517× (z -12.1, q 4e-31, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC13]] (+0.83, fdr 7e-06), [[CALU]] (+0.79, fdr 7e-06), [[KDELR2]] (+0.79, fdr 7e-06); moves opposite to [[USP24]] (-0.67, fdr 3e-05), [[ARID1B]] (-0.62, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HDLBP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15467.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (LOX-IMVI 2.92×, Panc 03.27 2.67×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.4 | 6e-08 | 34/48 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.9 | 2e-04 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +4.3 | 0.003 | 30/49 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.26× | +3.1 | 0.31 | 20/48 (LOX-IMVI, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15467.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -12.1 | 4e-31 | 45/48 (A498, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.579×** | -9.9 | 8e-21 | 37/47 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.517×** | -8.7 | 5e-16 | 42/48 (SW 1088, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.649×** | -5.9 | 4e-07 | 36/48 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.644×** | -5.8 | 7e-07 | 37/48 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -5.6 | 2e-06 | 36/48 (SNU-423, A-427, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.691×** | -5.1 | 3e-05 | 36/48 (J82, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.718×** | -4.5 | 4e-04 | 27/48 (NCI-H2347, H4, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -4.5 | 4e-04 | 29/49 (SW 900, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.721×** | -4.5 | 4e-04 | 28/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.726×** | -4.4 | 6e-04 | 29/48 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.757×** | -3.8 | 0.006 | 29/48 (Hs 766T, NCI-H661, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.010 | 27/48 (A498, CFPAC-1, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.773×** | -3.5 | 0.016 | 24/48 (LS 180, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.757×** | -3.5 | 0.016 | 23/47 (SW48, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.791×** | -3.2 | 0.045 | 18/48 (KATO III, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 116 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.8) |
| [[H4 (line)]] | wt | 152 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 50.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -16.5) |
| [[RKO (line)]] | wt | 44.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -9.9) |
| [[A-427 (line)]] | wt | 63.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 65.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.1) |
| [[J82 (line)]] | alt | 161 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 57.8 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.67× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -11.4) |
| [[SW 1088 (line)]] | alt | 101 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0347× (z -10.9) |
| [[SW 900 (line)]] | alt | 81.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.9) |
| [[SW1417 (line)]] | alt | 58.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.7) |
| [[A498 (line)]] | wt | 94.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -15.3) |
| [[HT-29 (line)]] | alt | 62.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -8.8) |
| [[LoVo (line)]] | wt | 52.3 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.260× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 33.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.92× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 40.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.8) |
| [[SNU-1 (line)]] | wt | 51.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -11.5) |
| [[SW48 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[A-172 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 87.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC13]] | +0.83 | +0.88 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 803 |
| [[CALU]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.79 | +0.81 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 651 |
| [[COPA]] | +0.78 | +0.81 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 622 |
| [[SEC61A1]] | +0.78 | +0.80 / +0.74 | both halves | 7e-06 | pathway: Antigen processing-Cross presentation; STRING 564 |
| [[SEC24D]] | +0.77 | +0.85 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 728 |
| [[COPB1]] | +0.77 | +0.81 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 781 |
| [[COG6]] | +0.77 | +0.78 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC31A]] | +0.75 | +0.79 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 791 |
| [[TMED9]] | +0.75 | +0.78 / +0.62 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 790 |
| [[CYB561D2]] | +0.74 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP24]] | -0.67 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[ARID1B]] | -0.62 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SEC22B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDLBP]] | C | SEC22B's natural level strengthens HDLBP's drug response | SEC22B's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.07; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.2, -32.0); signed map (-52.1, 8.6). **Vector** length 134, 41.5% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *COPI-mediated anterograde transport* (reactome, mean cos +0.66 to 9); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.65 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.73 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.8 | +6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.1 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.3 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.8 | -9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -12.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.8 | -5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | SEC22 homolog B, vesicle trafficking protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:120,150,898-120,176,520 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERS-24; previously SEC22L1 |
| Gene groups (HGNC) | SNAREs |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 14 pathways, smallest: Cargo concentration in the ER; COPII-mediated vesicle transport; ER-Phagosome pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O75396](https://www.uniprot.org/uniprotkb/O75396) (Vesicle-trafficking protein SEC22b):

> SNARE involved in targeting and fusion of ER-derived transport vesicles with the Golgi complex as well as Golgi-derived retrograde transport vesicles with the ER.

**Summary**, from NCBI Gene [9554](https://www.ncbi.nlm.nih.gov/gene/9554):

> The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:10700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10700) · Entrez [9554](https://www.ncbi.nlm.nih.gov/gene/9554) · UniProt [O75396](https://www.uniprot.org/uniprotkb/O75396) · Ensembl [ENSG00000265808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265808)

## Data

Gene col 15467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15467); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15467]; `tensor/DDL_lfc|DDL_z.npy` [15467]; `embed/gene_vectors.npy` [15467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15467 or target_col == 15467). Every well: [[SEC22B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC22B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
