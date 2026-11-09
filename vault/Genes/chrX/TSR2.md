---
symbol: "TSR2"
type: "gene"
col: 8169
ensembl_id: "ENSG00000158526"
name: "TSR2 ribosome maturation factor"
location: "Xp11.22"
module: 135
arm: "+"
pooled_cpm: 28.52
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# TSR2

*TSR2 ribosome maturation factor* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.96× (z +16.4, q 0e+00, up in 35 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +7.9, q 4e-13, up in 36 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRNP27]] (+0.69, fdr 2e-05), [[UBXN4]] (+0.69, fdr 1e-05), [[RNF6]] (+0.68, fdr 9e-05); moves opposite to [[HYAL2]] (-0.64, fdr 3e-05), [[CD320]] (-0.62, fdr 7e-05), [[NHP2]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8169.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.96×** | +16.4 | 0e+00 | 35/36 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.91×** | +13.2 | 1e-37 | 42/43 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +11.9 | 2e-30 | 37/38 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +8.0 | 2e-13 | 40/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.9 | 4e-13 | 36/47 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +7.8 | 6e-13 | 36/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.70×** | +6.4 | 2e-08 | 37/48 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.1 | 9e-08 | 36/47 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.40×** | +5.8 | 3e-07 | 33/47 (A549, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +5.8 | 3e-07 | 36/48 (NCI-H460, SW480, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.58×** | +5.7 | 8e-07 | 30/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +5.4 | 3e-06 | 28/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +5.3 | 6e-06 | 35/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.1 | 1e-05 | 30/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +4.6 | 2e-04 | 32/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.3 | 7e-04 | 21/48 (NCI-H2030, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.027 | 23/48 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +2.9 | 0.082 | 19/48 (NCI-H1573, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8169.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tadalafil (drug)]] 5 µM |  | 0.737× | -3.6 | 0.17 | 22/47 (HOP62, BT-474, …) | top dose only |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.818× | -3.4 | 0.19 | 19/48 (Hs 766T, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8169. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 52.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +15.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 35.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.16× (z +13.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 57.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 16.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +12.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 25.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +13.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +13.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 26.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 45.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 27.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +9.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.93× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +9.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.50× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8169), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP27]] | +0.69 | +0.80 / +0.48 | both halves | 2e-05 |  |
| [[UBXN4]] | +0.69 | +0.77 / +0.50 | both halves | 1e-05 |  |
| [[RNF6]] | +0.68 | +0.77 / +0.37 | both halves | 9e-05 |  |
| [[METTL6]] | +0.64 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[ARFGAP2]] | +0.63 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[CCT6P3]] | +0.63 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ACIN1]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZFR]] | +0.62 | +0.64 / +0.39 | both halves | 6e-05 |  |
| [[SLC4A1AP]] | +0.62 | +0.78 / +0.45 | both halves | 3e-05 |  |
| [[UPF3B]] | +0.62 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.61 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[TYW3]] | +0.61 | +0.69 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYAL2]] | -0.64 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[CD320]] | -0.62 | -0.63 / -0.38 | both halves | 7e-05 |  |
| [[NHP2]] | -0.58 | -0.57 / -0.33 | both halves | 1e-04 | STRING 720 |
| [[SLC35B2]] | -0.55 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[CTXN1]] | -0.55 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[PODXL2]] | -0.54 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[SNRPD2]] | -0.53 | -0.60 / -0.23 | both halves | 5e-04 |  |
| [[SLC66A2]] | -0.53 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[CD81]] | -0.53 | -0.60 / -0.36 | both halves | 9e-05 |  |
| [[C20orf27]] | -0.52 | -0.54 / -0.21 | both halves | 7e-04 |  |
| [[EML4]] | -0.52 | -0.53 / -0.26 | both halves | 4e-04 |  |
| [[KIAA1958]] | -0.52 | -0.55 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ARMCX4]] | B | ARMCX4 activity raises TSR2's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 1.26× lower at baseline in the lines without ARMCX4 | 0.056 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-19.1, 9.1); signed map (8.1, -29.8). **Vector** length 65.3, 13.5% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +7.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +4.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.3 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.1 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | TSR2 ribosome maturation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:54,440,404-54,448,032 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DT1P1A10, RP1-112K5.2, WGG1 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969E8](https://www.uniprot.org/uniprotkb/Q969E8) (Pre-rRNA-processing protein TSR2 homolog):

> May be involved in 20S pre-rRNA processing.

**Summary**, from NCBI Gene [90121](https://www.ncbi.nlm.nih.gov/gene/90121):

> The protein encoded by this gene appears to repress the transcription of NF-kappaB and may be involved in apoptosis. Defects in this gene are a cause of Diamond-Blackfan anemia. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:25455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25455) · Entrez [90121](https://www.ncbi.nlm.nih.gov/gene/90121) · UniProt [Q969E8](https://www.uniprot.org/uniprotkb/Q969E8) · Ensembl [ENSG00000158526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158526)

## Data

Gene col 8169: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8169); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8169, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8169]; `tensor/DDL_lfc|DDL_z.npy` [8169]; `embed/gene_vectors.npy` [8169]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8169 or target_col == 8169). Every well: [[TSR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
