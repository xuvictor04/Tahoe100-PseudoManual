---
symbol: "MZF1-AS1"
type: "gene"
col: 15580
ensembl_id: "ENSG00000267858"
name: "MZF1 antisense RNA 1"
location: "19q13.43"
module: 80
arm: "+"
pooled_cpm: 8.17
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# MZF1-AS1

*MZF1 antisense RNA 1* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.06× (z +17.8, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.702× (z -4.0, q 0.020, down in 13 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC90B-AS1]] (+0.82, fdr 7e-06), [[NEK8]] (+0.81, fdr 2e-05), [[KRCC1]] (+0.81, fdr 7e-06); moves opposite to [[FAM118A]] (-0.74, fdr 9e-05), [[MAST3]] (-0.73, fdr 2e-04), [[STX7]] (-0.72, fdr 2e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.06×** | +17.8 | 0e+00 | 40/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +17.2 | 0e+00 | 41/43 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +10.7 | 2e-24 | 34/40 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +9.3 | 2e-18 | 33/41 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +8.5 | 2e-15 | 35/45 (A-172, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.1 | 2e-10 | 27/47 (A-172, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.3 | 2e-08 | 30/43 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +5.8 | 4e-07 | 26/45 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.8 | 5e-07 | 9/18 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +4.8 | 8e-05 | 10/23 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 0.001 | 15/45 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.001 | 17/46 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.5 | 0.018 | 13/40 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.3 | 0.035 | 12/30 (NCI-H2347, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.047 | 5/46 (A-172, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -4.0 | 0.020 | 13/45 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.703×** | -4.0 | 0.020 | 11/47 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.724×** | -3.6 | 0.053 | 16/47 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.733×** | -3.5 | 0.065 | 12/47 (SNU-423, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | 0.751× | -3.2 | 0.14 | 9/47 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 13.3 | 0 | 3 | — | [[Methotrexate (drug)]] 0.5 µM 0.0556× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 6.92 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 13.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.3) | [[Digitoxin (drug)]] 5 µM 0.172× (z -13.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 13.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +13.5) | — |
| [[NCI-H2347 (line)]] | alt | 2.59 | 0 | 2 | — | [[Flutamide (drug)]] 0.05 µM 0.0589× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 8.38 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +10.5) | [[Talc (drug)]] 0.05 µM 0.0686× (z -9.4) |
| [[SW480 (line)]] | alt | 6.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +10.7) | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 9.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +11.1) | — |
| [[C32 (line)]] | wt | 8.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 8.71 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.0842× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.192× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 4.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 4.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 5.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +8.7) | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 6.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 6.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 6.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 8.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +9.8) | — |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | +0.82 | +0.81 / +0.58 | both halves | 7e-06 | same gene group |
| [[NEK8]] | +0.81 | +0.86 / +0.47 | both halves | 2e-05 |  |
| [[KRCC1]] | +0.81 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[LINC00571]] | +0.80 | +0.79 / +0.48 | both halves | 2e-05 |  |
| [[GPR137]] | +0.80 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.80 | +0.80 / +0.48 | both halves | 2e-05 | same gene group |
| [[TMEM202-AS1]] | +0.80 | +0.80 / +0.45 | both halves | 3e-05 | same gene group |
| [[PCNX4-DT]] | +0.79 | +0.83 / +0.41 | both halves | 4e-05 |  |
| [[PPP3CB-AS1]] | +0.78 | +0.79 / +0.41 | both halves | 4e-05 | same gene group |
| [[RAB30-DT]] | +0.78 | +0.81 / +0.49 | both halves | 1e-05 |  |
| [[C2orf49-DT]] | +0.78 | +0.85 / +0.49 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.77 | +0.77 / +0.44 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.74 | -0.72 / -0.36 | both halves | 9e-05 |  |
| [[MAST3]] | -0.73 | -0.66 / -0.31 | both halves | 2e-04 |  |
| [[STX7]] | -0.72 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[BRAT1]] | -0.72 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.70 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[ARRB2]] | -0.70 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[NBPF3]] | -0.69 | -0.68 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MZF1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLCO1B1]] | B | SLCO1B1 activity raises MZF1-AS1's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.34× lower at baseline in the lines without SLCO1B1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.848). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.0, 12.9); signed map (23.0, -7.0). **Vector** length 84.6, 16.2% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +17.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.5 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +17.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | -0.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.7 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MZF1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.43 — chr19:58,559,125-58,574,797 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51271) · Entrez [100131691](https://www.ncbi.nlm.nih.gov/gene/100131691) · Ensembl [ENSG00000267858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267858)

## Data

Gene col 15580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15580); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15580]; `tensor/DDL_lfc|DDL_z.npy` [15580]; `embed/gene_vectors.npy` [15580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15580 or target_col == 15580). Every well: [[MZF1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MZF1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
