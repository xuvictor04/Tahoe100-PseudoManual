---
symbol: "GRM8"
type: "gene"
col: 11047
ensembl_id: "ENSG00000179603"
name: "glutamate metabotropic receptor 8"
location: "7q31.33"
module: 75
arm: "+"
pooled_cpm: 6.11
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# GRM8

*glutamate metabotropic receptor 8* — 7q31.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 12.9× (z +39.6, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.709× (z -3.8, q 0.047, down in 8 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPP6]] (+0.85, fdr 7e-06), [[CLVS1]] (+0.82, fdr 7e-06), [[DKK2]] (+0.79, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **12.9×** | +39.6 | 0e+00 | 37/39 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.85×** | +27.4 | 0e+00 | 32/37 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **6.17×** | +20.0 | 0e+00 | 35/41 (C32, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.63×** | +15.0 | 0e+00 | 34/46 (C32, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.46×** | +13.1 | 4e-37 | 25/32 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.22×** | +12.4 | 3e-33 | 29/46 (A498, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.05×** | +12.2 | 2e-32 | 27/35 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.26×** | +12.0 | 3e-31 | 6/8 (HOP62, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +11.8 | 2e-30 | 3/5 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.98×** | +11.5 | 5e-29 | 25/36 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.84×** | +11.5 | 1e-28 | 33/42 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +10.8 | 1e-25 | 11/20 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.07×** | +8.0 | 7e-14 | 23/39 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +7.6 | 2e-12 | 23/42 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.25×** | +6.8 | 5e-10 | 16/40 (LoVo, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +5.2 | 6e-06 | 16/45 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +5.1 | 1e-05 | 12/33 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +5.0 | 2e-05 | 9/40 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -3.8 | 0.047 | 8/42 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 5 µM |  | **0.711×** | -3.8 | 0.047 | 9/43 (hTERT-HPNE, HepG2/C3A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -3.6 | 0.070 | 9/47 (HCT15, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.070 | 3/45 (RKO, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 9.26 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +13.6) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0751× (z -9.0) |
| [[LoVo (line)]] | wt | 5.18 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.1× (z +17.3) | — |
| [[SK-MEL-2 (line)]] | alt | 5.54 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.6× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 66.3 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0709× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.134× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 4.79 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +9.2) | — |
| [[A-172 (line)]] | wt | 2.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 2.33 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.1× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 2.65 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.9× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 4.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 3.86 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.5× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 6.54 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +15.9) | — |
| [[NCI-H460 (line)]] | wt | 4.85 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +16.0) | — |
| [[PANC-1 (line)]] | alt | 2.08 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +12.9) | — |
| [[A498 (line)]] | wt | 4.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.9× (z +15.7) | — |
| [[A549 (line)]] | wt | 2.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.8× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.8× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 2.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 2.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +9.3) | — |
| [[J82 (line)]] | alt | 2.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.1× (z +11.2) | — |
| [[KATO III (line)]] | alt | 2.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 2.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 1.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.50× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 1.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +8.9) | — |
| [[RKO (line)]] | wt | 24.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.49× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 2.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 2.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.3× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 4.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.76× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 3.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +8.5) | — |
| [[A-427 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP6]] | +0.85 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.82 | +0.74 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_SPERMATOGENESIS |
| [[DKK2]] | +0.79 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.78 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[NEB]] | +0.77 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.77 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[GRM7]] | +0.77 | +0.66 / +0.74 | both halves | 7e-06 | pathway: Class C/3 (Metabotropic glutamate/pheromone receptors); STRING 936 |
| [[DYNLRB2-AS1]] | +0.77 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[CIBAR1-DT]] | +0.76 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.76 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[LINC01811]] | +0.75 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[CCDC26]] | +0.75 | +0.62 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GRM8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[POU6F2]] | B | POU6F2 activity raises GRM8's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.88× lower at baseline in the lines without POU6F2 | 0.056 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[LY96]] | B | LY96 activity raises GRM8's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without LY96 | 0.064 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |
| [[LINC02428]] | B | LINC02428 activity raises GRM8's level | lines that do not express LINC02428 (32) vs lines expressing it (18) | 1.74× lower at baseline in the lines without LINC02428 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ENSG00000287598, ENSG00000287474 |
| [[CASC20]] | B | CASC20 activity raises GRM8's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without CASC20 | 0.086 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | GRM8's natural level weakens CLVS1's drug response | GRM8's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.70, reverse -0.34; direction clear | 0.033 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.875). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.7, 27.6); signed map (34.2, 13.9). **Vector** length 78.7, 14.3% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.6 | +39.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.1 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.0 | +20.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.8 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +27.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +15.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.7 | +12.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +1.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.5 | +3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -3.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.8 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | +1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | glutamate metabotropic receptor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.33 — chr7:126,438,598-127,253,093 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLUR8, GPRC1H, mGlu8, MGLUR8 |
| Gene groups (HGNC) | Glutamate metabotropic receptors; MicroRNA protein coding host genes |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 5 pathways, smallest: Class C/3 (Metabotropic glutamate/pheromone receptors); G alpha (i) signalling events; GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [O00222](https://www.uniprot.org/uniprotkb/O00222) (Metabotropic glutamate receptor 8):

> G protein-coupled receptor for glutamate. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of down-stream effectors, such as adenylate cyclase. Signaling inhibits adenylate cyclase activity.

**Summary**, from NCBI Gene [2918](https://www.ncbi.nlm.nih.gov/gene/2918):

> L-glutamate is the major excitatory neurotransmitter in the central nervous system and activates both ionotropic and metabotropic glutamate receptors. Glutamatergic neurotransmission is involved in most aspects of normal brain function and can be perturbed in many neuropathologic conditions. The metabotropic glutamate receptors are a family of G protein-coupled receptors, that have been divided into 3 groups on the basis of sequence homology, putative signal transduction mechanisms, and …

**Accessions** — [HGNC:4600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4600) · Entrez [2918](https://www.ncbi.nlm.nih.gov/gene/2918) · UniProt [O00222](https://www.uniprot.org/uniprotkb/O00222) · Ensembl [ENSG00000179603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179603)

## Data

Gene col 11047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11047); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11047]; `tensor/DDL_lfc|DDL_z.npy` [11047]; `embed/gene_vectors.npy` [11047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11047 or target_col == 11047). Every well: [[GRM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
