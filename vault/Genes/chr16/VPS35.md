---
symbol: "VPS35"
type: "gene"
col: 914
ensembl_id: "ENSG00000069329"
name: "VPS35 retromer complex component"
location: "16q11.2"
module: 57
arm: "+"
pooled_cpm: 132.02
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# VPS35

*VPS35 retromer complex component* — 16q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.70× (z +9.7, q 1e-19, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.38× (z +5.9, q 7e-07, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.737× (z -7.4, q 1e-10, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE3]] (+0.72, fdr 7e-06), [[BLTP1]] (+0.69, fdr 7e-06), [[APPL1]] (+0.67, fdr 7e-06); moves opposite to [[AGER]] (-0.54, fdr 4e-05), [[NANOS3]] (-0.48, fdr 1e-04), [[KIFC3]] (-0.47, fdr 9e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +9.7 | 1e-19 | 41/49 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.3 | 4e-14 | 34/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +5.9 | 7e-07 | 32/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +5.7 | 2e-06 | 32/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 5e-06 | 33/48 (A-427, PANC-1, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.3 | 1e-05 | 30/49 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +5.1 | 3e-05 | 32/48 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.6 | 4e-04 | 28/50 (NCI-H23, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.004 | 29/48 (A-427, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.25×** | +3.7 | 0.011 | 23/45 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.067 | 23/47 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.737×** | -7.4 | 1e-10 | 33/48 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -7.3 | 1e-10 | 35/48 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -5.7 | 2e-06 | 32/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.738×** | -5.6 | 4e-06 | 29/48 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.765×** | -4.9 | 1e-04 | 33/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.773×** | -4.7 | 2e-04 | 30/48 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.792×** | -4.3 | 0.002 | 31/49 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.804×** | -3.8 | 0.009 | 26/48 (A-172, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.821×** | -3.6 | 0.019 | 25/47 (hTERT-HPNE, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.11 | 17/48 (KATO III, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 139 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 1.87× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.629× (z -8.8) |
| [[BT-474 (line)]] | alt | 116 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.0) |
| [[SHP-77 (line)]] | alt | 160 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +11.1) | — |
| [[A-172 (line)]] | wt | 220 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -12.0) |
| [[A498 (line)]] | wt | 157 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +14.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 202 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -10.2) |
| [[HS-578T (line)]] | alt | 131 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.20× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 230 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 129 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +10.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 92.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 85.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 161 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +10.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -15.9) |
| [[HepG2_C3A (line)]] | wt | 135 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.4) |
| [[HOP62 (line)]] | alt | 167 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -15.3) |
| [[Hs 766T (line)]] | wt | 189 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.14× (z +9.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 177 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 99.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.5) |
| [[SNU-423 (line)]] | alt | 165 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 131 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.9) | — |
| [[A-427 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 163 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 113 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 107 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE3]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[BLTP1]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[APPL1]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[MIGA1]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[DNAJC13]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 | same gene group; STRING 937 |
| [[SCAMP1]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[EIF2AK1]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[COA8]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[VPS26A]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 | pathway: Signaling by WNT; STRING 999 |
| [[NTAN1]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[VIPAS39]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGER]] | -0.54 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[NANOS3]] | -0.48 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[KIFC3]] | -0.47 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[SPTY2D1OS]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers VPS35's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.439). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.6, -16.8); signed map (-31.3, -23.8). **Vector** length 124, 40.1% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.1 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.0 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.0 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.9 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.1 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -7.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.3 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.8 | -1.7 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | VPS35 retromer complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q11.2 — chr16:46,656,132-46,689,518 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10752, MEM3, PARK17 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 2 pathways, smallest: WNT ligand biogenesis and trafficking; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QK1](https://www.uniprot.org/uniprotkb/Q96QK1) (Vacuolar protein sorting-associated protein 35):

> Acts as a component of the retromer cargo-selective complex (CSC). The CSC is believed to be the core functional component of retromer or respective retromer complex variants acting to prevent missorting of selected transmembrane cargo proteins into the lysosomal degradation pathway. The recruitment of the CSC to the endosomal membrane involves RAB7A and SNX3. The CSC seems to associate with the cytoplasmic domain of cargo proteins predominantly via VPS35; however, these interactions seem to be …

**Summary**, from NCBI Gene [55737](https://www.ncbi.nlm.nih.gov/gene/55737):

> This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studies in yeast and mammalian cells indicate that this protein interacts directly with VPS35, which …

**Accessions** — [HGNC:13487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13487) · Entrez [55737](https://www.ncbi.nlm.nih.gov/gene/55737) · UniProt [Q96QK1](https://www.uniprot.org/uniprotkb/Q96QK1) · Ensembl [ENSG00000069329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069329)

## Data

Gene col 914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 914); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 914]; `tensor/DDL_lfc|DDL_z.npy` [914]; `embed/gene_vectors.npy` [914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 914 or target_col == 914). Every well: [[VPS35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
