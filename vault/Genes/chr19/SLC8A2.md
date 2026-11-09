---
symbol: "SLC8A2"
type: "gene"
col: 3965
ensembl_id: "ENSG00000118160"
name: "solute carrier family 8 member A2"
location: "19q13.32"
module: 53
arm: "+"
pooled_cpm: 3.91
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# SLC8A2

*solute carrier family 8 member A2* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 13.4× (z +30.2, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.640× (z -5.3, q 7e-05, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPERD]] (+0.74, fdr 7e-06), [[KPTN]] (+0.74, fdr 7e-06, ⚠ same locus), [[MIR9-1HG]] (+0.72, fdr 7e-06), [[ELAVL3]] (+0.72, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **13.4×** | +30.2 | 0e+00 | 33/33 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **6.72×** | +22.2 | 0e+00 | 31/35 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **6.39×** | +15.3 | 0e+00 | 34/41 (HT-29, SW480, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.44×** | +10.2 | 4e-22 | 30/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.33×** | +9.9 | 5e-21 | 19/31 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.12×** | +9.4 | 8e-19 | 29/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +7.8 | 4e-13 | 15/31 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.68×** | +7.8 | 5e-13 | 1/3 (C32) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.30×** | +6.8 | 5e-10 | 23/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +6.1 | 5e-08 | 18/36 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +6.0 | 1e-07 | 18/43 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.17×** | +5.9 | 2e-07 | 2/5 (A498, BT-474) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.4 | 2e-06 | 9/43 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.90×** | +5.3 | 6e-06 | 17/44 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +5.2 | 7e-06 | 17/39 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.71×** | +4.1 | 0.001 | 11/40 (A549, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.007 | 4/44 (LoVo, A498, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.05 µM |  | **1.47×** | +3.1 | 0.049 | 4/44 (LoVo, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.640×** | -5.3 | 7e-05 | 21/42 (SNU-423, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.587×** | -4.5 | 0.002 | 14/40 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.704×** | -4.2 | 0.005 | 18/43 (C32, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.629×** | -3.9 | 0.014 | 12/44 (COLO 205, KATO III, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.439×** | -3.6 | 0.037 | 12/31 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.676× | -3.1 | 0.17 | 8/35 (NCI-H23, A498, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 11.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.58× (z +10.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0694× (z -9.8) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.192× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 1.40 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 96.6× (z +14.8) | — |
| [[HT-29 (line)]] | alt | 4.78 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +11.5) | — |
| [[J82 (line)]] | alt | 2.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.8× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 3.41 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 6.39 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +11.3) | — |
| [[SW480 (line)]] | alt | 2.56 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +13.5) | — |
| [[A-172 (line)]] | wt | 1.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.0× (z +9.4) | — |
| [[A498 (line)]] | wt | 3.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +9.2) | — |
| [[A549 (line)]] | wt | 3.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.2× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[CFPAC-1 (line)]] | alt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.1× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 2.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.6× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 0.986 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.2× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 1.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 2.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 37.6× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 2.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 31.6× (z +8.8) | — |
| [[KATO III (line)]] | alt | 1.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.5× (z +9.0) | — |
| [[LoVo (line)]] | wt | 5.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.2× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 3.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 4.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 6.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 1.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 6.65 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0990× (z -8.8) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 2.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 2.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 34.1× (z +10.8) | — |
| [[A-427 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERD]] | +0.74 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[KPTN]] | +0.74 | +0.75 / +0.63 | both halves | 7e-06 | ⚠ same locus (3.3 kb, same strand: neighbours can correlate without regulation) |
| [[MIR9-1HG]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.72 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.72 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.71 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[PLA2G12B]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.71 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.71 | +0.73 / +0.65 | both halves | 7e-06 | pathway: Muscle contraction |
| [[ITGA9]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[EPHA1-AS1]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC8A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | B | ABL1 activity raises SLC8A2's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HPN]] | B | HPN activity raises SLC8A2's level | lines that do not express HPN (6) vs lines expressing it (44) | 2.08× lower at baseline in the lines without HPN | 0.048 | ⚠ within organs, on part of the lines; also absent: NAT14, APBA1; maybe low, not absent |
| [[F2]] | B | F2 activity raises SLC8A2's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without F2 | 0.099 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.6, -15.1); signed map (20.7, 12.0). **Vector** length 80.3, 14.7% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +30.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.7 | +15.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +22.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +6.7 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.9 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +4.1 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.6 | -5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 8 member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,428,017-47,471,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NCX2, KIAA1087 |
| Gene groups (HGNC) | Solute carrier family 8 |
| Reactome | 11 pathways, smallest: Sodium/Calcium exchangers; Reduction of cytosolic Ca++ levels; Platelet calcium homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPR5](https://www.uniprot.org/uniprotkb/Q9UPR5) (Sodium/calcium exchanger 2):

> Mediates the electrogenic exchange of Ca(2+) against Na(+) ions across the cell membrane, and thereby contributes to the regulation of cytoplasmic Ca(2+) levels and Ca(2+)-dependent cellular processes. Contributes to cellular Ca(2+) homeostasis in excitable cells. Contributes to the rapid decrease of cytoplasmic Ca(2+) levels back to baseline after neuronal activation, and thereby contributes to modulate synaptic plasticity, learning and memory. Plays a role in regulating urinary Ca(2+) and …

**Summary**, from NCBI Gene [6543](https://www.ncbi.nlm.nih.gov/gene/6543):

> Predicted to enable calcium:monoatomic cation antiporter activity involved in regulation of postsynaptic cytosolic calcium ion concentration and calcium:sodium antiporter activity. Predicted to be involved in several processes, including learning or memory; monoatomic cation transmembrane transport; and regulation of short-term neuronal synaptic plasticity. Predicted to act upstream of or within several processes, including modulation of chemical synaptic transmission; regulation of action …

**Accessions** — [HGNC:11069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11069) · Entrez [6543](https://www.ncbi.nlm.nih.gov/gene/6543) · UniProt [Q9UPR5](https://www.uniprot.org/uniprotkb/Q9UPR5) · Ensembl [ENSG00000118160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118160)

## Data

Gene col 3965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3965); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3965]; `tensor/DDL_lfc|DDL_z.npy` [3965]; `embed/gene_vectors.npy` [3965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3965 or target_col == 3965). Every well: [[SLC8A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC8A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
