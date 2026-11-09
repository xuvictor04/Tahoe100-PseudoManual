---
symbol: "ELF4"
type: "gene"
col: 2205
ensembl_id: "ENSG00000102034"
name: "E74 like ETS transcription factor 4"
location: "Xq26.1"
module: 54
arm: "-"
pooled_cpm: 22.58
n_lines_expressing: 47
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# ELF4

*E74 like ETS transcription factor 4* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.41× (z +4.3, q 0.007, up in 20 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.307× (z -14.7, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PXDC1]] (+0.63, fdr 3e-05), [[PPP1R18]] (+0.58, fdr 1e-05), [[MOB3C]] (+0.58, fdr 2e-05); moves opposite to [[PIBF1]] (-0.60, fdr 3e-05), [[TOMM20]] (-0.52, fdr 5e-05), [[GUSBP1]] (-0.52, fdr 1e-04).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARHGAP23]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[Niclosamide (olamine) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.007 | 20/44 (HOP62, SW48, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.007 | 25/42 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.026 | 21/44 (SNU-423, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.30× | +3.3 | 0.15 | 15/44 (SW480, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | 1.30× | +3.2 | 0.18 | 18/44 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2205.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.307×** | -14.7 | 0e+00 | 41/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.325×** | -14.0 | 3e-42 | 41/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.441×** | -10.2 | 3e-22 | 35/44 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.623×** | -5.9 | 5e-07 | 27/35 (HS-578T, A498, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.628×** | -5.8 | 6e-07 | 27/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.670×** | -4.8 | 1e-04 | 18/29 (HEC-1-A, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.663×** | -4.8 | 2e-04 | 19/33 (A498, PANC-1, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -3.9 | 0.006 | 20/45 (HT-29, NCI-H2347, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -3.8 | 0.011 | 3/45 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.754×** | -3.4 | 0.036 | 18/43 (AsPC-1, HS-578T, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.605×** | -3.3 | 0.052 | 12/40 (SW48, A-172, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 50.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -15.2) |
| [[HS-578T (line)]] | alt | 23.0 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -11.6) |
| [[J82 (line)]] | alt | 31.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 51.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -11.2) |
| [[HT-29 (line)]] | alt | 50.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -11.7) |
| [[SNU-423 (line)]] | alt | 23.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.245× (z -8.8) |
| [[SW480 (line)]] | alt | 36.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -14.4) |
| [[A-172 (line)]] | wt | 16.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -9.9) |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -12.3) |
| [[Hs 766T (line)]] | wt | 34.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -12.1) |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 2 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.137× (z -9.5) |
| [[A-427 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0880× (z -13.5) ⚠ cell-cycle shift, explains ~80% of this change |
| [[A549 (line)]] | wt | 19.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -9.8) |
| [[C32 (line)]] | wt | 6.04 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0751× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -8.9) |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0713× (z -12.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HepG2_C3A (line)]] | wt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.7) | — |
| [[KATO III (line)]] | alt | 28.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 34.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -9.1) |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.1) |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 1 | — | [[Demeclocycline (drug)]] 0.05 µM 0.0594× (z -9.3) |
| [[AN3 CA (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXDC1]] | +0.63 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[PPP1R18]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MOB3C]] | +0.58 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SEPTIN8]] | +0.56 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[RIPOR1]] | +0.53 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP23]] | +0.53 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SRC]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[HSPB8]] | +0.52 | +0.43 / +0.38 | both halves | 7e-05 |  |
| [[ZNF267]] | +0.52 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[PIEZO1]] | +0.51 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[PLEKHG3]] | +0.51 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[GCNT4]] | +0.50 | +0.23 / +0.40 | both halves | 5e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIBF1]] | -0.60 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[TOMM20]] | -0.52 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[GUSBP1]] | -0.52 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[AUH]] | -0.51 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[RALGAPA2]] | -0.49 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ACAD10]] | -0.49 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[FNTB]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[IFT172]] | -0.48 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[GUSBP1-1]] | -0.48 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[GLG1]] | -0.48 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[TYW1]] | -0.47 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[FAM172A]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP23]] | B | ARHGAP23 activity raises ELF4's level | lines that do not express ARHGAP23 (12) vs lines expressing it (38) | 1.94× lower at baseline in the lines without ARHGAP23 | 0.012 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ELF4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ELF4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | ELF4 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express ELF4 (3) vs lines expressing it (45) | the lines without ELF4: 0.35× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, SP100; maybe low, not absent |
| [[RIC1]] | C | ELF4 activity raises RIC1's level | lines that do not express ELF4 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without ELF4 | 0.038 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, SP100; maybe low, not absent |
| [[PPP1R12B]] | C | ELF4 activity strengthens PPP1R12B's drug response | lines that do not express ELF4 (3) vs lines expressing it (46) | the lines without ELF4 respond 0.48× as strongly (z diff +2.53); strongest at Homoharringtonine 5 µM: 1.39x vs 0.59x (z diff +10.8) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, SP100; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Auranofin (drug)]] 5 µM | C | ELF4 activity raises the cells' numbers under Auranofin 5 µM (protects the cells) | lines that do not express ELF4 (3) vs lines expressing it (45) | the lines without ELF4: 0.63× the cells of the other lines | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, SP100; maybe low, not absent |

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.392). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (14.5, 7.3); signed map (28.5, 9.7). **Vector** length 89.5, 20.0% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | -2.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +0.2 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -14.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -14.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | -10.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.9 | -2.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | E74 like ETS transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:130,063,955-130,110,716 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEF, ELFR |
| Gene groups (HGNC) | ETS transcription factor family |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99607](https://www.uniprot.org/uniprotkb/Q99607) (ETS-related transcription factor Elf-4):

> Transcriptional activator that binds to DNA sequences containing the consensus 5'-WGGA-3'. Transactivates promoters of the hematopoietic growth factor genes CSF2, IL3, IL8, and of the bovine lysozyme gene. Acts synergistically with RUNX1 to transactivate the IL3 promoter (By similarity). Transactivates the PRF1 promoter in natural killer (NK) cells and CD8+ T cells. Plays a role in the development and function of NK and NK T-cells and in innate immunity. Controls the proliferation and homing of …

**Summary**, from NCBI Gene [2000](https://www.ncbi.nlm.nih.gov/gene/2000):

> The protein encoded by this gene is a transcriptional activator that binds and activates the promoters of the CSF2, IL3, IL8, and PRF1 genes. The encoded protein is involved in natural killer cell development and function, innate immunity, and induction of cell cycle arrest in naive CD8+ cells. Two transcript variants encoding the same protein have been found for this gene.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:3319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3319) · Entrez [2000](https://www.ncbi.nlm.nih.gov/gene/2000) · UniProt [Q99607](https://www.uniprot.org/uniprotkb/Q99607) · Ensembl [ENSG00000102034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102034)

## Data

Gene col 2205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2205); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2205]; `tensor/DDL_lfc|DDL_z.npy` [2205]; `embed/gene_vectors.npy` [2205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2205 or target_col == 2205). Every well: [[ELF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
