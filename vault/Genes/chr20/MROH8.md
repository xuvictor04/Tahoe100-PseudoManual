---
symbol: "MROH8"
type: "gene"
col: 2123
ensembl_id: "ENSG00000101353"
name: "maestro heat like repeat family member 8"
location: "20q11.23"
module: 21
arm: "+"
pooled_cpm: 5.06
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MROH8

*maestro heat like repeat family member 8* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.04× (z +20.4, q 0e+00, up in 38 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.400× (z -6.8, q 6e-09, down in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cepharanthine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0822×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2CD5-AS1]] (+0.75, fdr 7e-06), [[GEMIN7-AS1]] (+0.74, fdr 7e-06), [[DNAJC27-AS1]] (+0.73, fdr 7e-06); moves opposite to [[RRP1B]] (-0.61, fdr 5e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.04×** | +20.4 | 0e+00 | 38/39 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **16.2×** | +19.8 | 0e+00 | 8/8 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **14.2×** | +18.8 | 0e+00 | 24/25 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **9.01×** | +12.5 | 2e-33 | 16/17 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +10.4 | 2e-23 | 31/40 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +6.1 | 9e-08 | 22/39 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +5.3 | 9e-06 | 23/31 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.81×** | +5.2 | 2e-05 | 5/10 (PANC-1, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +4.5 | 4e-04 | 17/36 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +4.5 | 4e-04 | 11/29 (J82, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +4.5 | 4e-04 | 14/35 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +4.4 | 4e-04 | 21/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.003 | 15/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.0 | 0.003 | 17/41 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +3.8 | 0.006 | 18/46 (SW1417, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.011 | 13/46 (PANC-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.015 | 17/46 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.60×** | +3.3 | 0.027 | 12/42 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +3.2 | 0.040 | 4/35 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.75×** | +3.0 | 0.081 | 6/44 (SW1417, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.73×** | +2.9 | 0.091 | 3/43 (BT-474, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2123.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cepharanthine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0822×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.400×** | -6.8 | 6e-09 | 30/47 (NCI-H23, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | 0.637× | -3.4 | 0.14 | 14/47 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.641× | -3.3 | 0.14 | 17/47 (CHP-212, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.628× | -3.3 | 0.14 | 11/47 (hTERT-HPNE, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.656× | -3.1 | 0.20 | 5/47 (SW1417, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 8.18 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.53× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 4.67 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.58× (z +16.2) | — |
| [[A498 (line)]] | wt | 3.26 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.5× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.76× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 2.89 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 8.69 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 16.7× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +8.9) | [[Cepharanthine (drug)]] 0.5 µM 0.0822× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 3.90 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.7× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.59× (z +9.4) | — |
| [[SW480 (line)]] | alt | 4.99 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.9× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.28× (z +12.9) | — |
| [[A549 (line)]] | wt | 6.43 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.4× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +8.8) | — |
| [[J82 (line)]] | alt | 7.40 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 20.2× (z +9.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 5.94 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 25.0× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 3.73 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 25.1× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.51× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 4.42 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.4× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.89× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 18.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +9.6) | — |
| [[A-172 (line)]] | wt | 3.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.47× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 2.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +9.1) | — |
| [[LoVo (line)]] | wt | 2.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.71× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 2.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.43× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 6.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.13× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 7.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.68× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +8.9) | — |
| [[A-427 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD5-AS1]] | +0.75 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[GEMIN7-AS1]] | +0.74 | +0.59 / +0.81 | both halves | 7e-06 |  |
| [[DNAJC27-AS1]] | +0.73 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.73 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[SPEN-AS1]] | +0.73 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SNAP25-AS1]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ANKHD1-DT]] | +0.73 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ZNF451-AS1]] | +0.72 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[PJVK]] | +0.72 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[KMT2E-AS1]] | +0.71 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SPATA21]] | +0.71 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[SUMO2P17]] | +0.70 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.61 | -0.50 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MROH8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.8, 25.2); signed map (32.4, -0.1). **Vector** length 77.1, 14.9% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.2 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +18.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +19.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +10.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | maestro heat like repeat family member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:37,101,226-37,179,588 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ621N11.4, dJ621N11.3; previously C20orf131, C20orf132 |
| Gene groups (HGNC) | Maestro heat like repeat containing |
| Matched by | ensembl_id |

UniProt [Q9H579](https://www.uniprot.org/uniprotkb/Q9H579) carries no function annotation.

**Summary**, from NCBI Gene [140699](https://www.ncbi.nlm.nih.gov/gene/140699):

> The protein encoded by this gene belongs to the maestro heat-like repeat family. The exact function of this gene is not known, however, in a genome-wide association study using hippocampal atrophy as a quantitative trait, this gene has been associated with Alzheimer's disease (PMID:19668339). Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:16125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16125) · Entrez [140699](https://www.ncbi.nlm.nih.gov/gene/140699) · UniProt [Q9H579](https://www.uniprot.org/uniprotkb/Q9H579) · Ensembl [ENSG00000101353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101353)

## Data

Gene col 2123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2123); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2123]; `tensor/DDL_lfc|DDL_z.npy` [2123]; `embed/gene_vectors.npy` [2123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2123 or target_col == 2123). Every well: [[MROH8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MROH8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
