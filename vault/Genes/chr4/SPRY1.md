---
symbol: "SPRY1"
type: "gene"
col: 8849
ensembl_id: "ENSG00000164056"
name: "sprouty RTK signaling antagonist 1"
location: "4q28.1"
module: 144
arm: "+"
pooled_cpm: 25.86
n_lines_expressing: 46
n_dd_up: 8
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# SPRY1

*sprouty RTK signaling antagonist 1* — 4q28.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.34× (z +7.9, q 2e-12, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.506× (z -8.5, q 1e-14, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K1]] (+0.55, fdr 1e-05), [[PHF21A]] (+0.55, fdr 1e-05), [[ZSWIM5]] (+0.54, fdr 1e-05); moves opposite to [[TANGO2]] (-0.51, fdr 3e-05), [[ADCY7]] (-0.50, fdr 4e-05), [[NUTM2A-AS1]] (-0.49, fdr 3e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01091]] → it (grade B ⚠); 4 go from it, the strongest it → [[RBPJ]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.34×** | +7.9 | 2e-12 | 33/44 (NCI-H23, C-33 A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.3 | 1e-07 | 23/37 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +6.1 | 2e-07 | 19/32 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.6 | 3e-06 | 18/38 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.018 | 19/43 (LoVo, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.031 | 19/44 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.067 | 15/44 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.30×** | +3.2 | 0.084 | 19/41 (SW480, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8849.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.506×** | -8.5 | 1e-14 | 37/43 (SNU-1, C32, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.496×** | -8.2 | 5e-14 | 34/43 (C32, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.661×** | -7.3 | 7e-11 | 26/43 (AN3 CA, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.564×** | -7.1 | 1e-10 | 30/43 (SW 900, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -6.8 | 2e-09 | 30/43 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.585×** | -6.7 | 2e-09 | 29/43 (RPMI-7951, SW 900, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.600×** | -6.1 | 6e-08 | 27/43 (SW 900, SW1417, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -5.8 | 4e-07 | 26/42 (SHP-77, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -5.2 | 1e-05 | 23/42 (MIA PaCa-2, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.669×** | -4.5 | 4e-04 | 25/44 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.703×** | -4.4 | 6e-04 | 21/43 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.777×** | -4.4 | 6e-04 | 17/44 (C32, J82, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.712×** | -4.2 | 0.001 | 21/43 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.713×** | -4.2 | 0.001 | 20/42 (SW 900, CFPAC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.721×** | -4.1 | 0.002 | 22/43 (SHP-77, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.564×** | -3.7 | 0.007 | 14/44 (SW1417, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.735×** | -3.7 | 0.008 | 18/43 (C32, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 73.3 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -15.3) |
| [[SHP-77 (line)]] | alt | 44.7 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -19.4) |
| [[SNU-1 (line)]] | wt | 244 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0801× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -17.9) |
| [[AN3 CA (line)]] | alt | 184 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -21.7) |
| [[C-33 A (line)]] | alt | 188 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 40.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 48.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -14.2) |
| [[SW 900 (line)]] | alt | 35.7 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.145× (z -11.2) |
| [[LoVo (line)]] | wt | 22.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.94× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 43.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 47.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +10.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.318× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 35.4 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 10.4× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -9.0) |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -8.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 84.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -9.0) |
| [[HOP62 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.70× (z +8.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.130× (z -8.5) |
| [[J82 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.248× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -12.3) |
| [[PANC-1 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 5.55 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K1]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PHF21A]] | +0.55 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ZSWIM5]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[IPMK]] | +0.54 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PIAS2]] | +0.54 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[HDHD5]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ETV1]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[TRIB2]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[EGLN1]] | +0.52 | +0.57 / +0.43 | both halves | 4e-05 |  |
| [[PIH1D1]] | +0.51 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[LRRC7]] | +0.50 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ZNF292]] | +0.50 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANGO2]] | -0.51 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ADCY7]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[NUTM2A-AS1]] | -0.49 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[KLC1]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RAB22A]] | -0.46 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[MAP4]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[VTI1A]] | -0.44 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[HSP90AA1]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[MICALL1]] | -0.44 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[LINC02614]] | -0.44 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[VCP]] | -0.43 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[UBR4]] | -0.43 | -0.44 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01091]] | B | LINC01091 activity raises SPRY1's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 2.79× lower at baseline in the lines without LINC01091 | 0.013 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[LINC01091]] | B | LINC01091 activity strengthens SPRY1's drug response | lines that do not express LINC01091 (12) vs lines expressing it (32) | the lines without LINC01091 respond 0.70× as strongly (z diff +1.46); strongest at Auranofin 5 µM: 0.60x vs 0.39x (z diff +3.4) | 0.054 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBPJ]] | C | SPRY1 activity strengthens RBPJ's drug response | lines that do not express SPRY1 (4) vs lines expressing it (45) | the lines without SPRY1 respond 0.68× as strongly (z diff +3.01); strongest at Belinostat 5 µM: 0.82x vs 0.62x (z diff +4.4) | 5e-04 | ⚠ few lines (4 vs 46); across organs; also absent: ARG2, ZNF385C, ENSG00000290927; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FOXN3]] | C | SPRY1 activity raises FOXN3's level | lines that do not express SPRY1 (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without SPRY1 | 0.023 | ⚠ few lines (4 vs 46); across organs; also absent: ARG2, ZNF385C, ENSG00000290927; maybe low, not absent |
| [[MICALL1]] | C | SPRY1 activity lowers MICALL1's level | lines that do not express SPRY1 (4) vs lines expressing it (46) | 1.83× higher at baseline in the lines without SPRY1 | 0.037 | ⚠ few lines (4 vs 46); across organs; also absent: ARG2, ZNF385C, ENSG00000290927; maybe low, not absent |
| [[ZSWIM5]] | C | SPRY1 activity raises ZSWIM5's level | lines that do not express SPRY1 (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without SPRY1 | 0.092 | ⚠ few lines (4 vs 46); across organs; also absent: ARG2, ZNF385C, ENSG00000290927; maybe low, not absent |

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, -20.3); signed map (-34.5, 31.5). **Vector** length 108, 26.9% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.8 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -8.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -7.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | sprouty RTK signaling antagonist 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.1 — chr4:123,396,795-123,403,760 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hSPRY1 |
| Gene groups (HGNC) | Sprouty RTK signaling antagonist family |
| Reactome | 3 pathways, smallest: EGFR downregulation; Signaling by EGFR; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [O43609](https://www.uniprot.org/uniprotkb/O43609) (Protein sprouty homolog 1):

> Inhibits fibroblast growth factor (FGF)-induced retinal lens fiber differentiation, probably by inhibiting FGF-mediated phosphorylation of ERK1/2 (By similarity). Inhibits TGFB-induced epithelial-to-mesenchymal transition in lens epithelial cells (By similarity).

**Summary**, from NCBI Gene [10252](https://www.ncbi.nlm.nih.gov/gene/10252):

> Predicted to enable protein kinase inhibitor activity. Involved in negative regulation of fibroblast growth factor receptor signaling pathway. Predicted to be located in plasma membrane. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11269) · Entrez [10252](https://www.ncbi.nlm.nih.gov/gene/10252) · UniProt [O43609](https://www.uniprot.org/uniprotkb/O43609) · Ensembl [ENSG00000164056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164056)

## Data

Gene col 8849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8849); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8849]; `tensor/DDL_lfc|DDL_z.npy` [8849]; `embed/gene_vectors.npy` [8849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8849 or target_col == 8849). Every well: [[SPRY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
