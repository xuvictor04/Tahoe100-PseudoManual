---
symbol: "SEC13"
type: "gene"
col: 8036
ensembl_id: "ENSG00000157020"
name: "SEC13 homolog, nuclear pore and COPII component"
location: "3p25.3"
module: 56
arm: "+"
pooled_cpm: 86.99
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 32
n_dd_up_clean: 5
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SEC13

*SEC13 homolog, nuclear pore and COPII component* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.24× (z +6.9, q 2e-09, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.491× (z -15.9, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDELR2]] (+0.85, fdr 7e-06), [[SEC24D]] (+0.85, fdr 7e-06), [[DHDDS]] (+0.83, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[PMM2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +6.9 | 2e-09 | 41/49 (HS-578T, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +6.9 | 2e-09 | 36/48 (SHP-77, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.1 | 7e-05 | 32/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +4.3 | 0.003 | 25/48 (hTERT-HPNE, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.003 | 26/48 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.8 | 0.015 | 27/48 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.7 | 0.016 | 21/44 (HEC-1-A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.022 | 13/49 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.11 | 19/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.11 | 16/48 (SNU-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 1.43× | +3.1 | 0.11 | 14/48 (HS-578T, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.13 | 17/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.491×** | -15.9 | 0e+00 | 47/49 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.515×** | -14.8 | 0e+00 | 44/47 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -10.6 | 7e-24 | 45/48 (HOP62, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.519×** | -10.3 | 7e-23 | 44/48 (AsPC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.664×** | -9.4 | 1e-18 | 44/48 (NCI-H2347, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.693×** | -8.3 | 9e-15 | 47/48 (A-172, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -7.7 | 8e-13 | 38/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.631×** | -7.5 | 4e-12 | 30/48 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.648×** | -7.1 | 8e-11 | 30/47 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -7.1 | 8e-11 | 37/50 (H4, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.651×** | -7.0 | 1e-10 | 30/48 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -6.8 | 4e-10 | 27/44 (SNU-1, H4, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.649×** | -6.8 | 5e-10 | 36/48 (J82, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.671×** | -6.5 | 3e-09 | 36/48 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.680×** | -6.2 | 2e-08 | 35/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.759×** | -6.2 | 3e-08 | 33/48 (HOP62, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 143 | 0 | 11 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -22.0) |
| [[SW 900 (line)]] | alt | 108 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -17.8) |
| [[HS-578T (line)]] | alt | 129 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.2) |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -16.8) |
| [[A498 (line)]] | wt | 103 | 0 | 8 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 137 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -20.6) |
| [[AsPC-1 (line)]] | alt | 98.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -20.9) |
| [[H4 (line)]] | wt | 165 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -23.8) |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -23.8) |
| [[J82 (line)]] | alt | 102 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -15.5) |
| [[Hs 766T (line)]] | wt | 98.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -15.2) |
| [[A-172 (line)]] | wt | 93.5 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -15.3) |
| [[SW1417 (line)]] | alt | 112 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -12.5) |
| [[HCT15 (line)]] | alt | 135 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -8.8) |
| [[HT-29 (line)]] | alt | 59.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 55.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 93.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.6) |
| [[SNU-1 (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.7) |
| [[A-427 (line)]] | wt | 58.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -9.2) |
| [[BT-474 (line)]] | alt | 56.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 57.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.1) |
| [[CHP-212 (line)]] | wt | 66.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 82.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.5) |
| [[LoVo (line)]] | wt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 63.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -8.7) |
| [[NCI-H596 (line)]] | alt | 88.7 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.307× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 124 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -8.5) |
| [[SW480 (line)]] | alt | 72.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.1) |
| [[A549 (line)]] | wt | 92.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 85.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR2]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 409 |
| [[SEC24D]] | +0.85 | +0.88 / +0.79 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[DHDDS]] | +0.83 | +0.83 / +0.81 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC22B]] | +0.83 | +0.88 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 803 |
| [[TMEM39A]] | +0.82 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[COPA]] | +0.82 | +0.87 / +0.75 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 657 |
| [[PDXDC1]] | +0.81 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[COG6]] | +0.81 | +0.83 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC61A1]] | +0.80 | +0.84 / +0.77 | both halves | 7e-06 | STRING 682 |
| [[COPB1]] | +0.79 | +0.86 / +0.67 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 825 |
| [[PMM2]] | +0.79 | +0.82 / +0.82 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[GORASP2]] | +0.78 | +0.82 / +0.69 | both halves | 7e-06 | pathway: Mitotic Prophase; STRING 637 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SEC13's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers SEC13's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SNHG18]] | B | SNHG18 activity raises SEC13's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without SNHG18 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[OXNAD1]] | C | OXNAD1's natural level strengthens SEC13's drug response | OXNAD1's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.08; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMM2]] | C | SEC13's natural level strengthens PMM2's drug response | SEC13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.26; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[GOLT1B]] | C | SEC13's natural level strengthens GOLT1B's drug response | SEC13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.23; direction not clear | 0.028 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[COPA]] | C | SEC13's natural level strengthens COPA's drug response | SEC13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.08; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[KDELR2]] | C | SEC13's natural level strengthens KDELR2's drug response | SEC13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.40; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Irinotecan (drug)]] 0.5 µM | C | SEC13's natural level raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | SEC13's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71 | 0.250 over the table, 0.020 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, -32.8); signed map (-51.3, 9.5). **Vector** length 131, 47.2% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *protein secretion* (hallmark, mean cos +0.65 to 10); *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.69 to 9); *COPI-mediated anterograde transport* (reactome, mean cos +0.69 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.4 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | -5.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.2 | -7.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.3 | +3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.8 | +5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.8 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.4 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -14.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -9.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -6.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.2 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | SEC13 homolog, nuclear pore and COPII component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:10,293,131-10,321,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEC13R, npp-20; previously D3S1231E, SEC13L1 |
| Gene groups (HGNC) | WD repeat domain containing; Nucleoporins; GATOR2 subcomplex; Coat protein complex II |
| Reactome | 97 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; Antigen Presentation: Folding, assembly and peptide loading of class I MHC; IP3 and IP4 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [P55735](https://www.uniprot.org/uniprotkb/P55735) (Protein SEC13 homolog):

> Functions as a component of the nuclear pore complex (NPC) and the COPII coat. At the endoplasmic reticulum, SEC13 is involved in the biogenesis of COPII-coated vesicles. Required for the exit of adipsin (CFD/ADN), an adipocyte-secreted protein from the endoplasmic reticulum (By similarity).; As a component of the GATOR2 complex, functions as an activator of the amino acid-sensing branch of the mTORC1 signaling pathway. The GATOR2 complex indirectly activates mTORC1 through the inhibition of …

**Summary**, from NCBI Gene [6396](https://www.ncbi.nlm.nih.gov/gene/6396):

> The protein encoded by this gene belongs to the SEC13 family of WD-repeat proteins. It is a constituent of the endoplasmic reticulum and the nuclear pore complex. It has similarity to the yeast SEC13 protein, which is required for vesicle biogenesis from endoplasmic reticulum during the transport of proteins. Multiple alternatively spliced transcript variants have been found. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:10697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10697) · Entrez [6396](https://www.ncbi.nlm.nih.gov/gene/6396) · UniProt [P55735](https://www.uniprot.org/uniprotkb/P55735) · Ensembl [ENSG00000157020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157020)

## Data

Gene col 8036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8036); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8036]; `tensor/DDL_lfc|DDL_z.npy` [8036]; `embed/gene_vectors.npy` [8036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8036 or target_col == 8036). Every well: [[SEC13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
