---
symbol: "NPC2"
type: "gene"
col: 4091
ensembl_id: "ENSG00000119655"
name: "NPC intracellular cholesterol transporter 2"
location: "14q24.3"
module: 24
arm: "+"
pooled_cpm: 37.68
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NPC2

*NPC intracellular cholesterol transporter 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.81× (z +9.5, q 2e-18, up in 42 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +6.0, q 2e-07, up in 39 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABARAP]] (+0.77, fdr 7e-06, ⚠ GABARAP in the vector space only through flagged drug-doses), [[CUTA]] (+0.76, fdr 7e-06), [[MICU1]] (+0.72, fdr 7e-06), [[NEU1]] (+0.72, fdr 7e-06); moves opposite to [[NOLC1]] (-0.65, fdr 7e-06), [[MAK16]] (-0.63, fdr 1e-05), [[CCT5]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.81×** | +9.5 | 2e-18 | 42/42 (A498, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.38×** | +7.7 | 5e-12 | 32/36 (AsPC-1, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.01×** | +6.4 | 3e-08 | 42/46 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +6.1 | 2e-07 | 30/38 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.0 | 2e-07 | 39/46 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +5.6 | 2e-06 | 35/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +5.3 | 1e-05 | 36/47 (RKO, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.73×** | +5.0 | 4e-05 | 38/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +5.0 | 4e-05 | 33/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.67×** | +4.7 | 1e-04 | 31/47 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.59×** | +4.3 | 0.001 | 27/45 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.008 | 27/47 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.008 | 31/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.49×** | +3.6 | 0.011 | 23/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.4 | 0.022 | 29/43 (HepG2/C3A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.037 | 24/47 (SK-MEL-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.085 | 24/47 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.085 | 19/47 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +2.9 | 0.098 | 16/47 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.098 | 17/48 (LS 180, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.698× | -3.3 | 0.52 | 23/46 (RPMI-7951, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 17.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.76× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +8.7) | — |
| [[A498 (line)]] | wt | 34.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 25.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 52.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1573 (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2347 (line)]] | alt | 188 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.3) | — |
| [[A-172 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.35 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAP]] ⚠ | +0.77 | +0.73 / +0.72 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CUTA]] | +0.76 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[MICU1]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[NEU1]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ARF5]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SIRT2]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[GABARAPL2]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ATP6V0E1]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NENF]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CERT1]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[GLMP]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOLC1]] | -0.65 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[MAK16]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CCT5]] | -0.61 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.61 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.60 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[NAA15]] | -0.60 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[PGAM5]] | -0.60 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[IFRD2]] | -0.60 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[GTPBP4]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | -0.59 | -0.55 / -0.61 | both halves | 1e-05 | same gene group |
| [[PPIL1]] | -0.58 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[DDX21]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity lowers NPC2's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.53× higher at baseline in the lines without TERT | 0.034 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-8.6, -46.1); signed map (-10.9, 6.8). **Vector** length 89.7, 28.2% of its response variance represented; |z| ≥ 3 in 648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.2 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.2 | +5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.9 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.4 | +3.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.0 | +2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | NPC intracellular cholesterol transporter 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,476,192-74,494,177 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HE1, NP-C2, EDDM1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; MD-2 related lipid recognition domain containing |
| Reactome | 6 pathways, smallest: LDL clearance; Plasma lipoprotein clearance; Plasma lipoprotein assembly, remodeling, and clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [P61916](https://www.uniprot.org/uniprotkb/P61916) (NPC intracellular cholesterol transporter 2):

> Intracellular cholesterol transporter which acts in concert with NPC1 and plays an important role in the egress of cholesterol from the lysosomal compartment. Unesterified cholesterol that has been released from LDLs in the lumen of the late endosomes/lysosomes is transferred by NPC2 to the cholesterol-binding pocket in the N-terminal domain of NPC1. May bind and mobilize cholesterol that is associated with membranes. NPC2 binds cholesterol with a 1:1 stoichiometry. Can bind a variety of …

**Summary**, from NCBI Gene [10577](https://www.ncbi.nlm.nih.gov/gene/10577):

> This gene encodes a protein containing a lipid recognition domain. The encoded protein may function in regulating the transport of cholesterol through the late endosomal/lysosomal system. Mutations in this gene have been associated with Niemann-Pick disease, type C2 and frontal lobe atrophy. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14537) · Entrez [10577](https://www.ncbi.nlm.nih.gov/gene/10577) · UniProt [P61916](https://www.uniprot.org/uniprotkb/P61916) · Ensembl [ENSG00000119655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119655)

## Data

Gene col 4091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4091); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4091]; `tensor/DDL_lfc|DDL_z.npy` [4091]; `embed/gene_vectors.npy` [4091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4091 or target_col == 4091). Every well: [[NPC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
