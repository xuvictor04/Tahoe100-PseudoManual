---
symbol: "HOXD11"
type: "gene"
col: 4917
ensembl_id: "ENSG00000128713"
name: "homeobox D11"
location: "2q31.1"
module: 46
arm: "+"
pooled_cpm: 2.79
n_lines_expressing: 14
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# HOXD11

*homeobox D11* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.59× (z +11.7, q 1e-28, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +5.8, q 8e-07, up in 7 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 6 lines (A-172 0.146×, HOP62 0.0644×, J82 0.0970×, A498 0.179×, …; ⚠ cell-cycle shift, explains ~26% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (A498 0.0623×, A-172 0.0892×, HOP62 0.0809×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.158×; ⚠ cell-cycle shift, explains ~26% of this change); [[Belinostat (drug)]] 5 µM in 1 line (A-172 0.213×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXD10]] (+0.83, fdr 7e-06, ⚠ same locus), [[SHOX2]] (+0.67, fdr 1e-05), [[HOXB-AS1]] (+0.55, fdr 2e-04), [[ZNF442]] (+0.55, fdr 1e-04); moves opposite to [[SCART1]] (-0.50, fdr 2e-04), [[C13orf46]] (-0.48, fdr 1e-04), [[NDFIP2]] (-0.48, fdr 4e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXD10]] → it (grade C ⚠); 2 go from it, the strongest it → [[C2CD5-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.59×** | +11.7 | 1e-28 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.48×** | +10.2 | 7e-22 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.67×** | +8.5 | 3e-15 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.8 | 8e-07 | 7/10 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.71×** | +5.7 | 1e-06 | 2/8 (J82, HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.85×** | +5.2 | 2e-05 | 5/10 (A498, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.41×** | +4.6 | 3e-04 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +4.6 | 3e-04 | 4/7 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +4.4 | 8e-04 | 1/7 (A498) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.2 | 0.002 | 1/8 (J82) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.76×** | +4.2 | 0.002 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.96×** | +4.0 | 0.003 | 1/7 (SHP-77) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.93×** | +3.9 | 0.004 | 1/7 (SHP-77) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.55×** | +3.8 | 0.005 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +3.5 | 0.020 | 1/10 (HOP62) | top dose only | composition shift |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **1.74×** | +3.1 | 0.067 | 0/8 | inconsistent across doses | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.70×** | +3.1 | 0.067 | 0/7 | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.63×** | +2.9 | 0.091 | 3/9 (NCI-H23, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 6 lines (A-172 0.146×, HOP62 0.0644×, J82 0.0970×, A498 0.179×, …; ⚠ cell-cycle shift, explains ~26% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (A498 0.0623×, A-172 0.0892×, HOP62 0.0809×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.158×; ⚠ cell-cycle shift, explains ~26% of this change); [[Belinostat (drug)]] 5 µM in 1 line (A-172 0.213×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | 0.585× | -3.2 | 0.46 | 9/11 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.579× | -3.0 | 0.46 | 1/12 (NCI-H661) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 45.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0892× (z -13.9) |
| [[A498 (line)]] | wt | 11.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0623× (z -14.1) |
| [[HOP62 (line)]] | alt | 7.42 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0644× (z -10.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0809× (z -9.4) |
| [[J82 (line)]] | alt | 7.15 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0970× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 5.92 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0605× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 0.189 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 17 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXD10]] | +0.83 | +0.78 / +0.76 | both halves | 7e-06 | same gene group; STRING 999; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SHOX2]] | +0.67 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[HOXB-AS1]] | +0.55 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[ZNF442]] | +0.55 | +0.34 / +0.37 | both halves | 1e-04 |  |
| [[ACOT2]] | +0.55 | +0.22 / +0.49 | both halves | 6e-04 |  |
| [[LRRC4B]] | +0.55 | +0.60 / +0.29 | both halves | 2e-04 |  |
| [[LRRN2]] | +0.54 | +0.50 / +0.28 | both halves | 3e-04 |  |
| [[PROCA1]] | +0.52 | +0.35 / +0.42 | both halves | 1e-04 |  |
| [[KLRK1-AS1]] | +0.52 | +0.27 / +0.44 | both halves | 3e-04 |  |
| [[ZNF433]] | +0.52 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[FLT3LG]] | +0.52 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[ZNF563]] | +0.51 | +0.22 / +0.39 | both halves | 6e-04 |  |
| [[UPK2]] | +0.51 | +0.25 / +0.43 | both halves | 4e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCART1]] | -0.50 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[C13orf46]] | -0.48 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[NDFIP2]] | -0.48 | -0.26 / -0.37 | both halves | 4e-04 |  |
| [[APPL2]] | -0.45 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[CYP2E1]] | -0.45 | -0.29 / -0.28 | both halves | 3e-04 |  |
| [[TAF1B]] | -0.45 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[MICAL2]] | -0.44 | -0.27 / -0.33 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXD10]] | C | HOXD10 activity raises HOXD11's level | lines that do not express HOXD10 (33) vs lines expressing it (17) | 4.00× lower at baseline in the lines without HOXD10 | 6e-04 | ⚠ within organs, on part of the lines; also absent: HOXD11, TMEM52B, PHYHIPL; co-absent with the target |
| [[TMEM52B]] | C | TMEM52B activity raises HOXD11's level | lines that do not express TMEM52B (39) vs lines expressing it (11) | 4.65× lower at baseline in the lines without TMEM52B | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OLR1, HOXD11, ENSG00000230258; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2CD5-AS1]] | B | HOXD11 activity raises C2CD5-AS1's level | lines that do not express HOXD11 (36) vs lines expressing it (14) | 1.09× lower at baseline in the lines without HOXD11 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXD10, TMEM52B, OLR1 |
| [[HOXD10]] | C | HOXD11 activity raises HOXD10's level | lines that do not express HOXD11 (36) vs lines expressing it (14) | 11.99× lower at baseline in the lines without HOXD11 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXD10, TMEM52B, OLR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (4.1, 25.8); signed map (36.0, -4.3). **Vector** length 25.1, 6.34% of its response variance represented; |z| ≥ 3 in 212 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +10.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.8 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +1.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -0.9 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -0.9 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -0.8 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -3.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | homeobox D11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:176,104,216-176,109,754 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX4, HOX4F |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Formation of the ureteric bud; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [P31277](https://www.uniprot.org/uniprotkb/P31277) (Homeobox protein Hox-D11):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3237](https://www.ncbi.nlm.nih.gov/gene/3237):

> This gene belongs to the homeobox family of genes. The homeobox genes encode a highly conserved family of transcription factors that play an important role in morphogenesis in all multicellular organisms. Mammals possess four similar homeobox gene clusters, HOXA, HOXB, HOXC and HOXD, located on different chromosomes, consisting of 9 to 11 genes arranged in tandem. This gene is one of several homeobox HOXD genes located in a cluster on chromosome 2. Deletions that remove the entire HOXD gene …

**Accessions** — [HGNC:5134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5134) · Entrez [3237](https://www.ncbi.nlm.nih.gov/gene/3237) · UniProt [P31277](https://www.uniprot.org/uniprotkb/P31277) · Ensembl [ENSG00000128713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128713)

## Data

Gene col 4917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4917); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4917]; `tensor/DDL_lfc|DDL_z.npy` [4917]; `embed/gene_vectors.npy` [4917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4917 or target_col == 4917). Every well: [[HOXD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
