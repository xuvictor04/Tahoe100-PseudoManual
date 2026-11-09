---
symbol: "NEB"
type: "gene"
col: 11368
ensembl_id: "ENSG00000183091"
name: "nebulin"
location: "2q23.3"
module: 26
arm: "+"
pooled_cpm: 5.16
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# NEB

*nebulin* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.13× (z +27.3, q 0e+00, up in 36 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ritonavir (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0625×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SHP-77 0.359×); [[Nimesulide (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0701×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH12]] (+0.89, fdr 7e-06), [[INTS6-AS1]] (+0.87, fdr 7e-06), [[PKD1L1]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.13×** | +27.3 | 0e+00 | 36/37 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.52×** | +22.2 | 0e+00 | 37/38 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **6.29×** | +16.9 | 0e+00 | 44/45 (NCI-H460, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.97×** | +16.5 | 0e+00 | 36/38 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +10.7 | 2e-24 | 17/21 (SHP-77, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.08×** | +10.0 | 2e-21 | 5/8 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.11×** | +9.7 | 2e-20 | 33/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +8.6 | 6e-16 | 24/36 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +8.4 | 4e-15 | 23/35 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +7.9 | 2e-13 | 6/11 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **4.29×** | +7.0 | 1e-10 | 26/44 (HepG2/C3A, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.13×** | +7.0 | 1e-10 | 28/45 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.10×** | +6.6 | 2e-09 | 23/44 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.3 | 1e-08 | 23/46 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.78×** | +5.3 | 4e-06 | 19/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.74×** | +5.1 | 1e-05 | 16/47 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +4.1 | 0.001 | 11/45 (SHP-77, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +4.0 | 0.002 | 17/46 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ritonavir (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0625×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SHP-77 0.359×); [[Nimesulide (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0701×; ⚠ unreliable plate only).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.81 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +15.1) | — |
| [[LoVo (line)]] | wt | 4.23 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.4× (z +18.2) | — |
| [[SW480 (line)]] | alt | 4.49 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +15.3) | — |
| [[NCI-H1573 (line)]] | alt | 3.25 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +9.1) | [[Ritonavir (drug)]] 0.5 µM 0.0625× (z -9.1) |
| [[A498 (line)]] | wt | 3.30 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 10.3× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 2.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 5.22 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 2.41 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +11.3) | — |
| [[A-172 (line)]] | wt | 2.00 | 1 | 0 | [[Auranofin (drug)]] 5 µM 35.3× (z +9.3) | — |
| [[A549 (line)]] | wt | 2.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +8.9) | — |
| [[C32 (line)]] | wt | 4.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +12.3) | — |
| [[HCT15 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 5.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 4.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.04× (z +10.1) | — |
| [[J82 (line)]] | alt | 3.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 2.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 4.25 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 20.8× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 3.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.40× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 4.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.07× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 4.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 67.5 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.359× (z -8.9) |
| [[SW 900 (line)]] | alt | 4.95 | 1 | 0 | [[Auranofin (drug)]] 5 µM 20.4× (z +8.8) | — |
| [[A-427 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH12]] | +0.89 | +0.89 / +0.83 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.87 | +0.86 / +0.77 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.86 | +0.87 / +0.83 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.86 | +0.86 / +0.64 | both halves | 7e-06 |  |
| [[ST8SIA5]] | +0.85 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.85 | +0.84 / +0.76 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.84 | +0.86 / +0.56 | both halves | 1e-05 |  |
| [[CIBAR1-DT]] | +0.83 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.83 | +0.88 / +0.51 | both halves | 1e-05 |  |
| [[H2AZ1-DT]] | +0.83 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[UNC79]] | +0.83 | +0.86 / +0.63 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.81 | +0.84 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NEB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C12orf50]] | B | C12orf50 activity strengthens NEB's drug response | lines that do not express C12orf50 (8) vs lines expressing it (39) | the lines without C12orf50 respond 0.83× as strongly (z diff +0.99); strongest at Homoharringtonine 5 µM: 3.01x vs 8.69x (z diff +3.8) | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC26A4]] | B | SLC26A4 activity strengthens NEB's drug response | lines that do not express SLC26A4 (7) vs lines expressing it (40) | the lines without SLC26A4 respond 0.56× as strongly (z diff +1.40); strongest at Homoharringtonine 5 µM: 3.26x vs 8.03x (z diff +3.3) | 0.076 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SYNPO2]] | B | SYNPO2 activity lowers NEB's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 1.60× higher at baseline in the lines without SYNPO2 | 0.081 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[LINC00705]] | B | LINC00705 activity lowers NEB's level | lines that do not express LINC00705 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without LINC00705 | 0.096 | ⚠ within organs, on part of the lines; also absent: SMAD3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.909). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.2, 16.5); signed map (24.2, 0.0). **Vector** length 81.8, 15.3% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.7 | +27.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.6 | +16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +22.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.4 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +3.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.6 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | nebulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:151,485,336-151,734,487 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NEB177D; previously NEM2 |
| Gene groups (HGNC) | Nebulin family; SH3 domain containing |
| Reactome | 2 pathways, smallest: Striated Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P20929](https://www.uniprot.org/uniprotkb/P20929) (Nebulin):

> This giant muscle protein may be involved in maintaining the structural integrity of sarcomeres and the membrane system associated with the myofibrils. Binds and stabilize F-actin.

**Summary**, from NCBI Gene [4703](https://www.ncbi.nlm.nih.gov/gene/4703):

> This gene encodes nebulin, a giant protein component of the cytoskeletal matrix that coexists with the thick and thin filaments within the sarcomeres of skeletal muscle. In most vertebrates, nebulin accounts for 3 to 4% of the total myofibrillar protein. The encoded protein contains approximately 30-amino acid long modules that can be classified into 7 types and other repeated modules. Protein isoform sizes vary from 600 to 800 kD due to alternative splicing that is tissue-, species-,and …

**Accessions** — [HGNC:7720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7720) · Entrez [4703](https://www.ncbi.nlm.nih.gov/gene/4703) · UniProt [P20929](https://www.uniprot.org/uniprotkb/P20929) · Ensembl [ENSG00000183091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183091)

## Data

Gene col 11368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11368); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11368]; `tensor/DDL_lfc|DDL_z.npy` [11368]; `embed/gene_vectors.npy` [11368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11368 or target_col == 11368). Every well: [[NEB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
