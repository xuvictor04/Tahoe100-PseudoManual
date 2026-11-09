---
symbol: "TEX21P"
type: "gene"
col: 13990
ensembl_id: "ENSG00000234911"
name: "testis expressed 21, pseudogene"
location: "14q23.3"
module: 26
arm: "+"
pooled_cpm: 9.95
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# TEX21P

*testis expressed 21, pseudogene* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +10.9, q 8e-25, up in 26 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.439× (z -9.5, q 9e-19, down in 27 of 38 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.488× (z -8.6, q 1e-15, down in 27 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESR2]] (+0.69, fdr 7e-06, ⚠ same locus), [[KPNB1-DT]] (+0.61, fdr 1e-05), [[PDC-AS1]] (+0.60, fdr 1e-05), [[CFAP53]] (+0.60, fdr 1e-05); moves opposite to [[PROSER1]] (-0.56, fdr 1e-05), [[FYCO1]] (-0.53, fdr 1e-05), [[VPS50]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC01762]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +10.9 | 8e-25 | 26/42 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.1 | 3e-07 | 20/41 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.9 | 2e-04 | 19/45 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.002 | 14/43 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.005 | 10/46 (SW480, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +3.6 | 0.036 | 15/46 (J82, H4, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.439×** | -9.5 | 9e-19 | 27/38 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.464×** | -8.9 | 2e-16 | 30/45 (HS-578T, A-427, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.488×** | -8.6 | 1e-15 | 27/43 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.493×** | -8.5 | 2e-15 | 31/45 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.288×** | -7.9 | 4e-13 | 28/46 (NCI-H23, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.530×** | -7.6 | 2e-12 | 27/45 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.539×** | -7.4 | 8e-12 | 24/43 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.531×** | -7.2 | 4e-11 | 27/44 (HEC-1-A, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.356×** | -6.5 | 5e-09 | 27/41 (hTERT-HPNE, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.632×** | -5.5 | 2e-06 | 20/42 (A549, HS-578T, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.468×** | -4.8 | 9e-05 | 21/40 (Hs 766T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -4.7 | 2e-04 | 17/45 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.685×** | -4.5 | 2e-04 | 21/46 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.696×** | -4.3 | 6e-04 | 22/45 (A549, HEC-1-A, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.699×** | -4.3 | 6e-04 | 19/34 (A549, RPMI-7951, …) | inconsistent across doses | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.729×** | -3.8 | 0.005 | 9/45 (NCI-H23, NCI-H2030, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.734×** | -3.7 | 0.006 | 13/46 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.008 | 15/46 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.744×** | -3.5 | 0.011 | 11/42 (LOX-IMVI, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Sonidegib (drug)]] 0.5 µM |  | **0.693×** | -3.1 | 0.042 | 13/45 (C32, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.756×** | -3.1 | 0.045 | 7/45 (CHP-212, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.772×** | -3.1 | 0.045 | 14/43 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.634×** | -2.9 | 0.086 | 5/35 (LS 180, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.844× | -2.9 | 0.086 | 9/46 (H4, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 31.5 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0565× (z -10.1) |
| [[A549 (line)]] | wt | 14.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0765× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0570× (z -13.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0777× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[H4 (line)]] | wt | 17.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Orlistat (drug)]] 0.05 µM 0.0791× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0973× (z -10.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.288× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.285× (z -8.5) |
| [[J82 (line)]] | alt | 8.81 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0746× (z -12.0) |
| [[PANC-1 (line)]] | alt | 6.22 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.221× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0791× (z -9.8) |
| [[A-427 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -10.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0947× (z -9.9) |
| [[LoVo (line)]] | wt | 8.53 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0368× (z -18.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 8.15 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 8.51 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -10.0) ⚠ toxic |
| [[SW480 (line)]] | alt | 8.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.1) | — |
| [[A-172 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESR2]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 | ⚠ same locus (8.1 kb, same strand: neighbours can correlate without regulation) |
| [[KPNB1-DT]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PDC-AS1]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RSPH9]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[TBCE-1]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[PSMD7-DT]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SNX31]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PELO-AS1]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LINC01422]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[C4orf47]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PROSER1]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[FYCO1]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[VPS50]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[PTGES2]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01762]] | B | LINC01762 activity raises TEX21P's level | lines that do not express LINC01762 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without LINC01762 | 0.013 | ⚠ within organs, on part of the lines; also absent: MPP4, LINC01429, DNAH6; maybe low, not absent |
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises TEX21P's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without CLDN14-AS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[SLC26A4]] | B | SLC26A4 activity raises TEX21P's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without SLC26A4 | 0.062 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (25.1, -15.1); signed map (26.7, -0.4). **Vector** length 67.9, 11.5% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +2.6 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +4.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -7.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.0 | -4.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -8.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -6.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 21, pseudogene |
| Locus type | pseudogene |
| Location | 14q23.3 — chr14:64,346,171-64,374,666 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:35455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35455) · Entrez [441687](https://www.ncbi.nlm.nih.gov/gene/441687) · Ensembl [ENSG00000234911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234911)

## Data

Gene col 13990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13990); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13990]; `tensor/DDL_lfc|DDL_z.npy` [13990]; `embed/gene_vectors.npy` [13990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13990 or target_col == 13990). Every well: [[TEX21P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX21P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
