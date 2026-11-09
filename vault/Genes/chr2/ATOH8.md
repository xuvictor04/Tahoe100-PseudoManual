---
symbol: "ATOH8"
type: "gene"
col: 9712
ensembl_id: "ENSG00000168874"
name: "atonal bHLH transcription factor 8"
location: "2p11.2"
module: 104
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 27
n_dd_up: 31
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# ATOH8

*atonal bHLH transcription factor 8* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.60× (z +8.4, q 4e-14, up in 5 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.549× (z -3.8, q 0.049, down in 6 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIPOR2]] (+0.68, fdr 1e-05), [[SLC7A2]] (+0.62, fdr 1e-05), [[DCN]] (+0.59, fdr 4e-05); moves opposite to [[CALM1]] (-0.48, fdr 7e-05), [[PKIA]] (-0.47, fdr 4e-05), [[ADAMTS16]] (-0.47, fdr 5e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SOX6]] → it (grade B ⚠); 7 go from it, the strongest it → [[KLF9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +8.4 | 4e-14 | 5/15 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.99×** | +8.3 | 4e-14 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +5.7 | 3e-06 | 1/3 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.39×** | +5.4 | 9e-06 | 10/18 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.37×** | +5.4 | 1e-05 | 14/19 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +4.5 | 7e-04 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.00×** | +4.3 | 0.001 | 10/20 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.08×** | +4.2 | 0.002 | 6/16 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +3.9 | 0.007 | 4/17 (SK-MEL-2, NCI-H2347, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.8 | 0.007 | 4/16 (NCI-H1792, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.007 | 1/22 (A-427) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +3.7 | 0.011 | 1/8 (NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.011 | 5/22 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.26×** | +3.6 | 0.013 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.76×** | +3.5 | 0.017 | 12/21 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.73×** | +3.4 | 0.025 | 6/19 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.14×** | +3.4 | 0.026 | 1/7 (NCI-H1792) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.78×** | +3.3 | 0.030 | 12/20 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.74×** | +3.2 | 0.045 | 7/19 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.050 | 11/21 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.054 | 2/16 (C32, HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.549×** | -3.8 | 0.049 | 6/19 (SW 900, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.551×** | -3.6 | 0.049 | 3/21 (SHP-77, SW 900, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.672×** | -3.6 | 0.049 | 7/20 (SNU-1, H4, …) | rises with dose | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.672×** | -3.6 | 0.049 | 7/21 (SK-MEL-2, HepG2/C3A, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.559×** | -3.5 | 0.049 | 6/19 (COLO 205, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.557×** | -3.4 | 0.061 | 9/19 (SNU-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.602× | -3.2 | 0.11 | 6/19 (SNU-1, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 87.2 | 0 | 10 (8 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0318× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.208× (z -9.8) |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0283× (z -13.5) |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0163× (z -13.2) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -9.3) |
| [[COLO 205 (line)]] | alt | 6.29 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.0359× (z -9.8) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0452× (z -8.6) |
| [[C32 (line)]] | wt | 5.58 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0506× (z -9.6) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 4.98 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0317× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.536 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.613 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.795 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.708 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.409 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPOR2]] | +0.68 | +0.55 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[SLC7A2]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[DCN]] | +0.59 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[MGP]] | +0.57 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[TMTC1]] | +0.56 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[ACSL1]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[UBE2E1]] | +0.55 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[PDGFRA]] | +0.55 | +0.40 / +0.62 | both halves | 4e-05 |  |
| [[GLUL]] | +0.55 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[KLF9]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZFHX3]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TNS2]] | +0.54 | +0.37 / +0.56 | both halves | 8e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALM1]] | -0.48 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[PKIA]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ADAMTS16]] | -0.47 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[UBA6]] | -0.47 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[EFL1]] | -0.46 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[C3orf52]] | -0.46 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[LRRC8C]] | -0.45 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[DUSP18]] | -0.45 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[RAB22A]] | -0.44 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[TMEM158]] | -0.44 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[MMP1]] | -0.43 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[DOP1B]] | -0.43 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX6]] | B | SOX6 activity raises ATOH8's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without SOX6 | 0.044 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises ATOH8's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF9]] | B | ATOH8 activity raises KLF9's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without ATOH8 | 0.011 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent |
| [[RHOBTB3]] | B | ATOH8 activity raises RHOBTB3's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without ATOH8 | 0.030 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent |
| [[ENPP2]] | B | ATOH8 activity raises ENPP2's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 2.51× lower at baseline in the lines without ATOH8 | 0.064 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent |
| [[ZNF608]] | B | ATOH8 activity raises ZNF608's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without ATOH8 | 0.088 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent |
| [[PDGFRA]] | C | ATOH8 activity raises PDGFRA's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 2.85× lower at baseline in the lines without ATOH8 | 0.051 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent; co-absent with the target |
| [[DAAM2]] | C | ATOH8 activity raises DAAM2's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without ATOH8 | 0.072 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent; co-absent with the target |
| [[LINC01098]] | C | ATOH8 activity raises LINC01098's level | lines that do not express ATOH8 (23) vs lines expressing it (27) | 2.37× lower at baseline in the lines without ATOH8 | 0.074 | ⚠ within organs, on part of the lines; also absent: DZIP1, LINC00839, KCNQ5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.0, 17.5); signed map (19.1, 31.4). **Vector** length 49.2, 10.8% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +8.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +5.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.0 | +5.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.7 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.0 | -1.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -0.9 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | atonal bHLH transcription factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,751,344-85,791,383 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HATH6, FLJ14708, bHLHa21 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SQ7](https://www.uniprot.org/uniprotkb/Q96SQ7) (Transcription factor ATOH8):

> Transcription factor that binds a palindromic (canonical) core consensus DNA sequence 5'-CANNTG- 3' known as an E-box element, possibly as a heterodimer with other bHLH proteins. Regulates endothelial cell proliferation, migration and tube-like structures formation. Modulates endothelial cell differentiation through NOS3. May be implicated in specification and differentiation of neuronal cell lineages in the brain (By similarity). May participate in kidney development and may be involved in …

**Summary**, from NCBI Gene [84913](https://www.ncbi.nlm.nih.gov/gene/84913):

> Enables DNA-binding transcription factor activity and E-box binding activity. Involved in several processes, including positive regulation of SMAD protein signal transduction; positive regulation of endothelial cell differentiation; and regulation of gene expression. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24126) · Entrez [84913](https://www.ncbi.nlm.nih.gov/gene/84913) · UniProt [Q96SQ7](https://www.uniprot.org/uniprotkb/Q96SQ7) · Ensembl [ENSG00000168874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168874)

## Data

Gene col 9712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9712); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9712]; `tensor/DDL_lfc|DDL_z.npy` [9712]; `embed/gene_vectors.npy` [9712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9712 or target_col == 9712). Every well: [[ATOH8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATOH8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
