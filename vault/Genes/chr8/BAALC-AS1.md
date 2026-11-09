---
symbol: "BAALC-AS1"
type: "gene"
col: 14479
ensembl_id: "ENSG00000247081"
name: "BAALC antisense RNA 1"
location: "8q22.3"
module: 26
arm: "+"
pooled_cpm: 14.82
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 9
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# BAALC-AS1

*BAALC antisense RNA 1* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.46× (z +14.2, q 9e-43, up in 38 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.613× (z -5.4, q 4e-05, down in 18 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.666× (z -4.5, q 0.002, down in 17 of 42 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC26A7]] (+0.79, fdr 7e-06), [[LINC02641]] (+0.78, fdr 7e-06), [[TPTE2]] (+0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02398]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MEF2C-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.46×** | +14.2 | 9e-43 | 38/44 (NCI-H460, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.8 | 4e-20 | 26/41 (AsPC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +9.3 | 4e-18 | 22/41 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +9.0 | 2e-17 | 26/42 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +8.2 | 4e-14 | 27/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.95×** | +6.5 | 1e-08 | 24/42 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +6.4 | 1e-08 | 28/44 (KATO III, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.8 | 6e-07 | 21/43 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.70×** | +5.7 | 7e-07 | 21/43 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.7 | 7e-07 | 19/42 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +5.5 | 2e-06 | 20/44 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.0 | 3e-05 | 19/45 (SHP-77, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +5.0 | 3e-05 | 22/44 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.28×** | +4.9 | 4e-05 | 18/43 (C32, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +4.5 | 3e-04 | 15/43 (NCI-H23, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 5e-04 | 19/45 (C-33 A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.613×** | -5.4 | 4e-05 | 18/37 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.666×** | -4.5 | 0.002 | 17/42 (CFPAC-1, RKO, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.706×** | -4.0 | 0.012 | 12/45 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.710×** | -3.9 | 0.012 | 15/45 (LoVo, HEC-1-A, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.726×** | -3.7 | 0.028 | 17/34 (A498, hTERT-HPNE, …) | inconsistent across doses | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.732×** | -3.6 | 0.032 | 12/44 (SK-MEL-2, NCI-H23, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.074 | 12/45 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.744×** | -3.3 | 0.074 | 14/44 (HepG2/C3A, SW48, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.676×** | -3.2 | 0.085 | 6/43 (C32, SW1417, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.62 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +14.3) | [[Roxadustat (drug)]] 0.05 µM 0.0857× (z -10.6) |
| [[A498 (line)]] | wt | 74.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.248× (z -8.6) |
| [[LoVo (line)]] | wt | 11.1 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.76× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 21.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[SW480 (line)]] | alt | 9.99 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.60× (z +10.1) | — |
| [[A-427 (line)]] | wt | 7.66 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0546× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 4.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +8.6) | — |
| [[C32 (line)]] | wt | 21.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +9.9) | — |
| [[H4 (line)]] | wt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0796× (z -10.7) |
| [[HOP62 (line)]] | alt | 20.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.27× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 61.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0788× (z -8.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0901× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H23 (line)]] | alt | 9.39 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.85× (z +8.7) | — |
| [[A-172 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A7]] | +0.79 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[LINC02641]] | +0.78 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TPTE2]] | +0.75 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[LINC01208]] | +0.73 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[MGC4859]] | +0.71 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[LINC02763]] | +0.69 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[MGAM]] | +0.69 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[COLQ]] | +0.67 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[ST8SIA5]] | +0.67 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[LINC01762]] | +0.66 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[GRK7]] | +0.66 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CMYA5]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02398]] | B | LINC02398 activity raises BAALC-AS1's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 2.31× lower at baseline in the lines without LINC02398 | 0.009 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises BAALC-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.29× lower at baseline in the lines without FSIP2-AS1 | 0.050 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity raises BAALC-AS1's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without LINC02641 | 0.078 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[ANKRD7]] | B | ANKRD7 activity raises BAALC-AS1's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without ANKRD7 | 0.081 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C-AS1]] | C | BAALC-AS1 activity raises MEF2C-AS1's level | lines that do not express BAALC-AS1 (3) vs lines expressing it (47) | 4.64× lower at baseline in the lines without BAALC-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SATB2, LCA5, MAMDC2-AS1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.6, 17.0); signed map (22.8, 1.0). **Vector** length 95.5, 20.5% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.0 | +14.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +9.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.0 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +6.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.7 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +1.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | BAALC antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q22.3 — chr8:103,153,394-103,298,772 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lncFZD6, FZD6-DT |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50461) · Entrez [100499183](https://www.ncbi.nlm.nih.gov/gene/100499183) · Ensembl [ENSG00000247081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247081)

## Data

Gene col 14479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14479); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14479]; `tensor/DDL_lfc|DDL_z.npy` [14479]; `embed/gene_vectors.npy` [14479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14479 or target_col == 14479). Every well: [[BAALC-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAALC-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
