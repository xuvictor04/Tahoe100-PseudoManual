---
symbol: "UBE2E3"
type: "gene"
col: 9896
ensembl_id: "ENSG00000170035"
name: "ubiquitin conjugating enzyme E2 E3"
location: "2q31.3"
module: 41
arm: "-"
pooled_cpm: 98.63
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# UBE2E3

*ubiquitin conjugating enzyme E2 E3* — 2q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 1.41× (z +4.3, q 0.009, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.433× (z -15.7, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGPS]] (+0.67, fdr 7e-06), [[DHX9]] (+0.63, fdr 1e-05), [[CHN1]] (+0.62, fdr 1e-05); moves opposite to [[DNAJC25]] (-0.63, fdr 1e-05), [[STX5-DT]] (-0.62, fdr 1e-05), [[RNMT]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +4.3 | 0.009 | 30/46 (SW48, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.043 | 23/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.050 | 26/48 (SW1417, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9896.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.433×** | -15.7 | 0e+00 | 45/48 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.498×** | -9.2 | 8e-18 | 43/47 (SW480, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.536×** | -8.3 | 3e-14 | 44/47 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.525×** | -8.2 | 3e-14 | 42/49 (SW 900, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.550×** | -7.9 | 3e-13 | 39/47 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.576×** | -7.0 | 2e-10 | 39/47 (NCI-H23, SW48, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.704×** | -6.6 | 4e-09 | 32/47 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.639×** | -5.9 | 2e-07 | 36/47 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.600×** | -3.5 | 0.026 | 27/47 (CFPAC-1, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.740×** | -3.2 | 0.067 | 22/47 (LOX-IMVI, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -3.1 | 0.094 | 21/47 (SW48, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | 0.786× | -3.1 | 0.10 | 21/43 (LOX-IMVI, C-33 A, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 155 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 324 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -20.1) |
| [[Panc 03.27 (line)]] | alt | 139 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -11.3) |
| [[SNU-1 (line)]] | wt | 103 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -13.7) |
| [[SW 900 (line)]] | alt | 181 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 85.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 160 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 123 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -11.1) |
| [[LS 180 (line)]] | wt | 76.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 93.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -17.0) |
| [[SW48 (line)]] | wt | 107 | 1 | 2 | [[TAK-901 (drug)]] 0.05 µM 3.25× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -13.2) |
| [[SW480 (line)]] | alt | 124 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -12.7) |
| [[C-33 A (line)]] | alt | 100.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 103 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -12.0) |
| [[HOP62 (line)]] | alt | 122 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -11.7) |
| [[HS-578T (line)]] | alt | 75.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -12.9) |
| [[HT-29 (line)]] | alt | 83.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 80.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 139 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 73.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 126 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 73.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -12.3) |
| [[A-172 (line)]] | wt | 98.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -11.2) |
| [[A-427 (line)]] | wt | 69.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 76.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.7) |
| [[A549 (line)]] | wt | 54.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -10.2) |
| [[BT-474 (line)]] | alt | 41.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.4) |
| [[C32 (line)]] | wt | 42.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.2) |
| [[CHP-212 (line)]] | wt | 99.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -11.1) |
| [[H4 (line)]] | wt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -10.6) |
| [[Hs 766T (line)]] | wt | 74.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 67.1 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0803× (z -9.7) |
| [[PANC-1 (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.8) |
| [[RKO (line)]] | wt | 80.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -10.7) |
| [[SHP-77 (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -16.3) |
| [[SK-MEL-2 (line)]] | alt | 79.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.289× (z -10.9) |
| [[SNU-423 (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -9.6) |
| [[SW1417 (line)]] | alt | 86.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -9.8) |
| [[AN3 CA (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGPS]] | +0.67 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[DHX9]] | +0.63 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[CHN1]] | +0.62 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MPDZ]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FAM98B]] | +0.61 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[MTMR2]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ZDHHC21]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CEP41]] | +0.56 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[VMA21]] | +0.56 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[NAA15]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TMEM33]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[KLHL2]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |

## Genes that move opposite

*66 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC25]] | -0.63 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[STX5-DT]] | -0.62 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[RNMT]] | -0.62 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[SRP54]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[PMS2P4-1]] | -0.61 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[NARF]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TULP3]] | -0.60 | -0.45 / -0.69 | both halves | 3e-05 |  |
| [[USP37]] | -0.57 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[KLC4]] | -0.57 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[BET1]] | -0.57 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[COG7]] | -0.57 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[FAM177A1]] | -0.57 | -0.57 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UBE2E3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (7.8, -39.8); signed map (12.4, -40.2). **Vector** length 125, 40.3% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +4.6 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.5 | +1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.3 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -15.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -7.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 E3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.3 — chr2:180,967,248-181,076,585 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UbcH9 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Protein ubiquitination; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969T4](https://www.uniprot.org/uniprotkb/Q969T4) (Ubiquitin-conjugating enzyme E2 E3):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-11'- and 'Lys-48'-, as well as 'Lys-63'-linked polyubiquitination. Participates in the regulation of transepithelial sodium transport in renal cells.

**Summary**, from NCBI Gene [10477](https://www.ncbi.nlm.nih.gov/gene/10477):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. The encoded protein shares 100% sequence identity with the mouse and rat counterparts, which indicates that …

**Accessions** — [HGNC:12479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12479) · Entrez [10477](https://www.ncbi.nlm.nih.gov/gene/10477) · UniProt [Q969T4](https://www.uniprot.org/uniprotkb/Q969T4) · Ensembl [ENSG00000170035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170035)

## Data

Gene col 9896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9896); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9896]; `tensor/DDL_lfc|DDL_z.npy` [9896]; `embed/gene_vectors.npy` [9896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9896 or target_col == 9896). Every well: [[UBE2E3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2E3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
