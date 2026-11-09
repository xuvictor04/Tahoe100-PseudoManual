---
symbol: "FAM182B"
type: "gene"
col: 10573
ensembl_id: "ENSG00000175170"
name: "family with sequence similarity 182 member B"
location: "20p11.1"
module: 43
arm: "+"
pooled_cpm: 6.03
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# FAM182B

*family with sequence similarity 182 member B* — 20p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.83× (z +8.2, q 1e-13, up in 29 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.554× (z -6.6, q 2e-08, down in 26 of 37 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.449× (z -6.3, q 7e-08, down in 27 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN6-DT]] (+0.74, fdr 1e-05), [[COMMD6]] (+0.71, fdr 3e-05), [[RPS19]] (+0.71, fdr 1e-05); moves opposite to [[PSME3]] (-0.70, fdr 2e-05), [[NUP188]] (-0.69, fdr 2e-05), [[WDR1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EID2B]] → it (grade B ⚠); 4 go from it, the strongest it → [[ZFP14]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10573.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.83×** | +8.2 | 1e-13 | 29/43 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.73×** | +7.9 | 6e-13 | 32/43 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.69×** | +7.8 | 9e-13 | 33/43 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +7.2 | 7e-11 | 31/42 (SW1417, HOP62, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +6.7 | 2e-09 | 25/40 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +5.7 | 2e-06 | 27/43 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.03×** | +5.6 | 2e-06 | 23/40 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.003 | 15/43 (KATO III, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.41×** | +3.9 | 0.007 | 10/43 (LoVo, SW 900, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **2.18×** | +3.2 | 0.067 | 11/44 (SW1417, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.067 | 11/39 (SW480, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.074 | 12/42 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.73×** | +3.1 | 0.080 | 5/37 (NCI-H1792, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10573.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.554×** | -6.6 | 2e-08 | 26/37 (SNU-423, A498, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.449×** | -6.3 | 7e-08 | 27/43 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.453×** | -6.2 | 8e-08 | 25/36 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.485×** | -5.7 | 2e-06 | 29/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -5.5 | 5e-06 | 20/35 (SNU-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.308×** | -4.9 | 1e-04 | 25/42 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -4.3 | 0.002 | 19/42 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.560×** | -4.2 | 0.002 | 9/14 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.598×** | -3.9 | 0.006 | 20/41 (A498, LS 180, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.611×** | -3.9 | 0.006 | 19/43 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -3.7 | 0.012 | 17/36 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -3.6 | 0.018 | 15/32 (SNU-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0808× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.157× (z -9.8) |
| [[A498 (line)]] | wt | 6.00 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -13.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -9.4) |
| [[A549 (line)]] | wt | 5.01 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.0735× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0918× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H1573 (line)]] | alt | 4.49 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0605× (z -10.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Orlistat (drug)]] 0.05 µM 0.0780× (z -8.6) |
| [[A-172 (line)]] | wt | 6.16 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0816× (z -8.5) |
| [[Hs 766T (line)]] | wt | 7.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0464× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 3.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -8.7) |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0613× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 6.10 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -15.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 900 (line)]] | alt | 6.01 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0499× (z -10.2) |
| [[A-427 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | +0.74 | +0.49 / +0.78 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.71 | +0.43 / +0.78 | both halves | 3e-05 |  |
| [[RPS19]] | +0.71 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[TOMM7]] | +0.71 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[RPL36]] | +0.69 | +0.46 / +0.76 | both halves | 2e-05 |  |
| [[CAMLG]] | +0.69 | +0.37 / +0.81 | both halves | 7e-05 |  |
| [[RPL35A]] | +0.69 | +0.44 / +0.74 | both halves | 3e-05 |  |
| [[ZFAND2A-DT]] | +0.68 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[RPS27]] | +0.68 | +0.39 / +0.76 | both halves | 6e-05 |  |
| [[RPL18]] ⚠ | +0.68 | +0.39 / +0.78 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS14]] | +0.68 | +0.37 / +0.74 | both halves | 7e-05 |  |
| [[NENF]] | +0.67 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[SNHG25]] | +0.67 | +0.45 / +0.72 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.70 | -0.46 / -0.80 | both halves | 2e-05 |  |
| [[NUP188]] | -0.69 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[WDR1]] | -0.65 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.65 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[AKAP11]] | -0.64 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[PDAP1]] | -0.63 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[VARS1]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ELK4]] | -0.62 | -0.37 / -0.75 | both halves | 9e-05 |  |
| [[NRAS]] | -0.60 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.60 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[CCT7]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[TWF1]] | -0.60 | -0.41 / -0.68 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | EID2B activity raises FAM182B's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without EID2B | 0.023 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[ZNF594-DT]] | B | ZNF594-DT activity raises FAM182B's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without ZNF594-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[LINC00173]] | B | LINC00173 activity raises FAM182B's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.20× lower at baseline in the lines without LINC00173 | 0.059 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |
| [[ZNF540]] | B | ZNF540 activity raises FAM182B's level | lines that do not express ZNF540 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without ZNF540 | 0.074 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZFP14, ZNF573; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFP14]] | C | FAM182B activity raises ZFP14's level | lines that do not express FAM182B (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without FAM182B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FGF12, SLFNL1-AS1; maybe low, not absent; its own permutation p |
| [[ZNF594-DT]] | C | FAM182B activity raises ZNF594-DT's level | lines that do not express FAM182B (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without FAM182B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FGF12, SLFNL1-AS1; maybe low, not absent; its own permutation p |
| [[SREK1IP1]] | C | FAM182B activity lowers SREK1IP1's level | lines that do not express FAM182B (4) vs lines expressing it (46) | 1.87× higher at baseline in the lines without FAM182B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FGF12, SLFNL1-AS1; maybe low, not absent; its own permutation p |
| [[CLDN12]] | C | FAM182B activity lowers CLDN12's level | lines that do not express FAM182B (4) vs lines expressing it (46) | 1.43× higher at baseline in the lines without FAM182B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FGF12, SLFNL1-AS1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-43.8, -25.3); signed map (-58.5, -1.9). **Vector** length 63.5, 11.6% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.51 to 55); *Peptide chain elongation* (reactome, mean cos +0.53 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.52 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +2.5 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.0 | +5.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.4 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.3 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.7 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -2.2 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | +0.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -0.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 182 member B |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20p11.1 — chr20:25,762,384-25,868,225 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with FAM root symbol |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:34503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34503) · Entrez [728882](https://www.ncbi.nlm.nih.gov/gene/728882) · Ensembl [ENSG00000175170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175170)

## Data

Gene col 10573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10573); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10573]; `tensor/DDL_lfc|DDL_z.npy` [10573]; `embed/gene_vectors.npy` [10573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10573 or target_col == 10573). Every well: [[FAM182B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM182B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
