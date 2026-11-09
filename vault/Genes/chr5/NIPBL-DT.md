---
symbol: "NIPBL-DT"
type: "gene"
col: 16175
ensembl_id: "ENSG00000285967"
name: "NIPBL divergent transcript"
location: "5p13.2"
module: 15
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# NIPBL-DT

*NIPBL divergent transcript* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.88× (z +25.6, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 0.676× (z -4.3, q 0.010, down in 15 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (RKO 0.0964×); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (Hs 766T 0.0833×); [[Almonertinib (mesylate) (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0567×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C2-AS2]] (+0.70, fdr 1e-05), [[PNISR-AS1]] (+0.69, fdr 3e-05), [[LINC00938]] (+0.68, fdr 1e-05); moves opposite to [[STX8]] (-0.67, fdr 1e-05), [[WDR70]] (-0.67, fdr 3e-05), [[CEP290]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.88×** | +25.6 | 0e+00 | 43/43 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.10×** | +11.9 | 2e-30 | 14/17 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.95×** | +11.8 | 4e-30 | 35/40 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +10.8 | 3e-25 | 6/8 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.60×** | +10.5 | 1e-23 | 16/26 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +10.1 | 7e-22 | 31/45 (RKO, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +8.5 | 1e-15 | 29/41 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +6.6 | 4e-09 | 16/47 (J82, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.4 | 1e-08 | 11/27 (LoVo, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.77×** | +6.1 | 7e-08 | 20/44 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.9 | 2e-07 | 20/48 (SW1417, HOP62, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +4.3 | 8e-04 | 8/40 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.2 | 9e-04 | 12/48 (NCI-H1573, HT-29, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.006 | 11/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.047 | 4/46 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.055 | 8/42 (SHP-77, SW1417, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.081 | 2/47 (RKO, LoVo) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (RKO 0.0964×); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (Hs 766T 0.0833×); [[Almonertinib (mesylate) (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0567×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.676×** | -4.3 | 0.010 | 15/45 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.734× | -3.5 | 0.12 | 11/38 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.754× | -3.2 | 0.24 | 11/46 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 5.98 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +8.5) | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0833× (z -9.2) |
| [[SW 900 (line)]] | alt | 5.15 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.08× (z +11.0) | [[Allantoin (drug)]] 0.05 µM 0.0941× (z -8.8) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 7.27 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.2) | — |
| [[A-172 (line)]] | wt | 4.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +10.5) | — |
| [[A498 (line)]] | wt | 4.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.06× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 2.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 7.30 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0778× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 2.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 4.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 6.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.91× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 5.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +10.4) | — |
| [[LoVo (line)]] | wt | 6.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 3.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 3.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 3.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.98× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 4.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 4.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +12.6) | — |
| [[RKO (line)]] | wt | 7.51 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0964× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 5.60 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0567× (z -9.1) |
| [[SW1417 (line)]] | alt | 5.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.95× (z +11.1) | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C2-AS2]] | +0.70 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PNISR-AS1]] | +0.69 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[LINC00938]] | +0.68 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ZNF596]] | +0.66 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[ZNF514]] | +0.66 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[MSL3]] | +0.65 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SNHG10]] | +0.64 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[ZNF213-AS1]] | +0.64 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[LAMTOR5-AS1]] | +0.63 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[RALY-AS1]] | +0.62 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[BHLHE40-AS1]] | +0.62 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[GAPLINC]] | +0.61 | +0.46 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX8]] | -0.67 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[WDR70]] | -0.67 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[CEP290]] | -0.60 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[ISCA2]] | -0.60 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[VPS8]] | -0.59 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[PUSL1]] | -0.59 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[TTBK2]] | -0.58 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[SFSWAP]] | -0.57 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[GPATCH11]] | -0.57 | -0.20 / -0.42 | both halves | 7e-04 |  |
| [[COMMD2]] | -0.57 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[KLF2]] | -0.57 | -0.47 / -0.29 | both halves | 3e-04 |  |
| [[WRAP73]] | -0.57 | -0.25 / -0.35 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NIPBL-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.9, 21.4); signed map (29.5, -16.7). **Vector** length 69.4, 10.7% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +25.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +11.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +4.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | NIPBL divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p13.2 — chr5:36,864,425-36,876,700 (-) |
| Ensembl biotype | lncRNA |
| Also known as | NIPBL-AS; previously NIPBL-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51293) · Entrez [646719](https://www.ncbi.nlm.nih.gov/gene/646719) · Ensembl [ENSG00000285967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000285967)

## Data

Gene col 16175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16175); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16175]; `tensor/DDL_lfc|DDL_z.npy` [16175]; `embed/gene_vectors.npy` [16175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16175 or target_col == 16175). Every well: [[NIPBL-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPBL-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
