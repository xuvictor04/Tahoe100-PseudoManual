---
symbol: "NQO1-DT"
type: "gene"
col: 15377
ensembl_id: "ENSG00000262136"
name: "NQO1 divergent transcript"
location: "16q22.1"
module: 26
arm: "+"
pooled_cpm: 7.57
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# NQO1-DT

*NQO1 divergent transcript* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.19× (z +21.7, q 0e+00, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.474× (z -8.1, q 4e-13, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC90B-AS1]] (+0.81, fdr 1e-05), [[CFAP70]] (+0.81, fdr 7e-06), [[TMEM202-AS1]] (+0.80, fdr 1e-05); moves opposite to [[BRAT1]] (-0.69, fdr 4e-05), [[YIF1B]] (-0.67, fdr 0.002, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.19×** | +21.7 | 0e+00 | 36/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.73×** | +16.0 | 0e+00 | 12/15 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +14.1 | 6e-43 | 37/42 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +13.6 | 6e-40 | 24/29 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.73×** | +13.0 | 1e-36 | 14/20 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.78×** | +10.9 | 7e-26 | 37/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.68×** | +10.6 | 4e-24 | 33/41 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +8.1 | 3e-14 | 27/39 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.8 | 4e-13 | 28/47 (A498, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +7.1 | 5e-11 | 22/47 (HEC-1-A, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +6.4 | 1e-08 | 25/44 (KATO III, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +6.1 | 5e-08 | 23/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.5 | 1e-06 | 24/42 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 6e-05 | 19/44 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +4.5 | 3e-04 | 17/43 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 8e-04 | 14/46 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.002 | 11/47 (SNU-1, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.002 | 17/45 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.474×** | -8.1 | 4e-13 | 28/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.478×** | -8.0 | 4e-13 | 33/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.469×** | -7.7 | 2e-12 | 27/45 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.734× | -3.2 | 0.18 | 6/46 (CHP-212, HS-578T, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.711× | -3.0 | 0.30 | 8/47 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 23.0 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.189× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 14.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 18.2× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.80× (z +10.9) | — |
| [[A498 (line)]] | wt | 7.02 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 9.99 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -8.9) |
| [[SW480 (line)]] | alt | 7.53 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +13.5) | — |
| [[A-172 (line)]] | wt | 4.90 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0706× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 5.36 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 9.99 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +12.4) | [[Harringtonine (drug)]] 0.05 µM 0.124× (z -10.0) |
| [[LoVo (line)]] | wt | 3.64 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +9.2) | [[Ferulic acid (drug)]] 5 µM 0.0524× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -9.8) |
| [[PANC-1 (line)]] | alt | 5.58 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +12.8) | — |
| [[A549 (line)]] | wt | 6.24 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0851× (z -9.3) |
| [[C32 (line)]] | wt | 4.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 9.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 4.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.54× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 4.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.54× (z +9.2) | — |
| [[J82 (line)]] | alt | 5.51 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0859× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 5.80 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0854× (z -8.8) |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.117× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 2.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 6.24 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.9× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 6.47 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 15.8× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | +0.81 | +0.79 / +0.55 | both halves | 1e-05 |  |
| [[CFAP70]] | +0.81 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.80 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.78 | +0.78 / +0.46 | both halves | 2e-05 |  |
| [[FBXL19-AS1]] | +0.77 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PTOV1-AS1]] | +0.77 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | +0.76 | +0.78 / +0.41 | both halves | 4e-05 |  |
| [[ZCWPW1]] | +0.76 | +0.75 / +0.44 | both halves | 3e-05 |  |
| [[NEB]] | +0.76 | +0.76 / +0.50 | both halves | 1e-05 |  |
| [[ZNF546]] | +0.75 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[AKT1S1]] | +0.74 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[ATE1OSP]] | +0.74 | +0.76 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.69 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[YIF1B]] | -0.67 | -0.62 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NQO1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises NQO1-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.806). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.1, 12.9); signed map (23.9, -3.8). **Vector** length 101, 22.6% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +21.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +16.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +6.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +2.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.7 | -7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.5 | -8.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.7 | -8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Salicylic acid (drug)]] 5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | NQO1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q22.1 — chr16:69,726,768-69,742,563 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FASRL |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55344) · Entrez [119139903](https://www.ncbi.nlm.nih.gov/gene/119139903) · Ensembl [ENSG00000262136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000262136)

## Data

Gene col 15377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15377); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15377]; `tensor/DDL_lfc|DDL_z.npy` [15377]; `embed/gene_vectors.npy` [15377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15377 or target_col == 15377). Every well: [[NQO1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NQO1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
