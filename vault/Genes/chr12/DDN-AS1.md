---
symbol: "DDN-AS1"
type: "gene"
col: 15072
ensembl_id: "ENSG00000257913"
name: "DDN and PRKAG1 antisense RNA 1"
location: "12q13.12"
module: 21
arm: "+"
pooled_cpm: 3.4
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# DDN-AS1

*DDN and PRKAG1 antisense RNA 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +8.6, q 4e-15, up in 20 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.565× (z -6.0, q 9e-07, down in 20 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.0911×, PANC-1 0.156×; ⚠ cell-cycle shift, explains ~11% of this change); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0562×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.206×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (HOP62 0.0709×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D22A-DT]] (+0.66, fdr 1e-05), [[POM121]] (+0.66, fdr 1e-05), [[SEPTIN1]] (+0.66, fdr 5e-05); moves opposite to [[VEZF1]] (-0.57, fdr 3e-05), [[ZNF678]] (-0.55, fdr 5e-05), [[FAM111A]] (-0.55, fdr 2e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +8.6 | 4e-15 | 20/35 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +8.4 | 2e-14 | 4/7 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +7.5 | 1e-11 | 2/5 (A498, HOP62) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.2 | 7e-08 | 7/19 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.8 | 2e-04 | 4/18 (KATO III, A498, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.5 | 8e-04 | 6/45 (SHP-77, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.005 | 12/42 (SW480, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.017 | 13/34 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.025 | 10/30 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.4 | 0.034 | 2/36 (CFPAC-1, J82) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.034 | 8/45 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.4 | 0.034 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.052 | 7/30 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.064 | 1/28 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15072.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.0911×, PANC-1 0.156×; ⚠ cell-cycle shift, explains ~11% of this change); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0562×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.206×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (HOP62 0.0709×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.565×** | -6.0 | 9e-07 | 20/41 (NCI-H1792, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.656×** | -4.6 | 1e-03 | 15/42 (NCI-H23, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.799×** | -3.5 | 0.090 | 17/36 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -3.4 | 0.094 | 7/47 (HS-578T, SNU-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.740× | -3.3 | 0.10 | 10/37 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.759× | -3.0 | 0.23 | 8/46 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.34 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -16.6) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -10.0) |
| [[HOP62 (line)]] | alt | 3.89 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0709× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 3.55 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0567× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 3.96 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0562× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0911× (z -18.6) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SHP-77 (line)]] | alt | 6.06 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0963× (z -8.6) |
| [[A-172 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D22A-DT]] | +0.66 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[POM121]] | +0.66 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SEPTIN1]] | +0.66 | +0.39 / +0.74 | both halves | 5e-05 |  |
| [[EFCAB14-AS1]] | +0.66 | +0.43 / +0.70 | both halves | 3e-05 | same gene group |
| [[RHOQ-AS1]] | +0.65 | +0.45 / +0.69 | both halves | 3e-05 | same gene group |
| [[NFATC2IP-AS1]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 | same gene group |
| [[CRLF1]] | +0.64 | +0.36 / +0.72 | both halves | 1e-04 |  |
| [[UBOX5-AS1]] | +0.63 | +0.44 / +0.66 | both halves | 3e-05 | same gene group |
| [[BIRC6-AS2-1]] | +0.63 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[MIR4458HG]] | +0.63 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[NDUFAF7]] | +0.63 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[SNHG21]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ZNF678]] | -0.55 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[FAM111A]] | -0.55 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[EFR3A]] | -0.54 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ARAF]] | -0.54 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[TIA1]] | -0.54 | -0.40 / -0.65 | both halves | 5e-05 |  |
| [[YTHDC2]] | -0.53 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[NHLRC2]] | -0.53 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[PEX1]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[OCRL]] | -0.52 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[AKAP11]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[PABIR1]] | -0.52 | -0.37 / -0.53 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DDN-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, 29.2); signed map (-43.6, 21.8). **Vector** length 36.0, 3.30% of its response variance represented; |z| ≥ 3 in 834 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -1.8 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -0.9 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | DDN and PRKAG1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q13.12 — chr12:48,998,367-49,019,241 (+) |
| Ensembl biotype | lncRNA |
| Also known as | CAT1507 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53464) · Entrez [105369758](https://www.ncbi.nlm.nih.gov/gene/105369758) · Ensembl [ENSG00000257913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257913)

## Data

Gene col 15072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15072); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15072]; `tensor/DDL_lfc|DDL_z.npy` [15072]; `embed/gene_vectors.npy` [15072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15072 or target_col == 15072). Every well: [[DDN-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDN-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
