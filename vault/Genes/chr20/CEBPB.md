---
symbol: "CEBPB"
type: "gene"
col: 10225
ensembl_id: "ENSG00000172216"
name: "CCAAT enhancer binding protein beta"
location: "20q13.13"
module: 113
arm: "+"
pooled_cpm: 39.84
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# CEBPB

*CCAAT enhancer binding protein beta* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.38× (z +7.1, q 8e-10, up in 33 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HT-29 0.178×, KATO III 0.147×, SNU-423 0.241×, CFPAC-1 0.254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.228×, SNU-423 0.334×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1F]] (+0.71, fdr 7e-06), [[IRX3]] (+0.70, fdr 7e-06), [[MT1M]] (+0.70, fdr 7e-06); moves opposite to [[BANF1]] (-0.54, fdr 2e-05), [[PGRMC1]] (-0.53, fdr 4e-05), [[CDH6]] (-0.51, fdr 3e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RHCG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.38×** | +7.1 | 8e-10 | 33/47 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +6.7 | 4e-09 | 42/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.66×** | +6.0 | 3e-07 | 27/47 (AsPC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +5.7 | 2e-06 | 31/47 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +5.5 | 5e-06 | 31/47 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +5.3 | 1e-05 | 40/48 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.88×** | +5.2 | 2e-05 | 30/48 (HOP62, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.81×** | +5.0 | 3e-05 | 31/48 (Panc 03.27, NCI-H2347, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.72×** | +4.6 | 3e-04 | 29/48 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.5 | 5e-04 | 31/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.69×** | +4.4 | 5e-04 | 35/48 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.64×** | +4.2 | 0.001 | 29/48 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.61×** | +4.1 | 0.002 | 21/48 (NCI-H2347, Hs 766T, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.56×** | +3.8 | 0.006 | 26/48 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.027 | 24/48 (LoVo, A-172, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.079 | 24/48 (NCI-H2347, Hs 766T, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +3.0 | 0.096 | 22/48 (SW480, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10225.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HT-29 0.178×, KATO III 0.147×, SNU-423 0.241×, CFPAC-1 0.254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.228×, SNU-423 0.334×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.220×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | 0.749× | -3.5 | 0.12 | 26/48 (A498, CFPAC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | 0.454× | -3.5 | 0.12 | 26/47 (SW 900, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.773× | -3.1 | 0.31 | 23/48 (Hs 766T, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 45.2 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +21.7) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.2× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 25.3 | 5 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.16× (z +10.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.66× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 42.4 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.85× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 35.5 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.07× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 81.4 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.40× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -11.2) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 33.9 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.95× (z +9.5) | — |
| [[A498 (line)]] | wt | 100 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -17.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +9.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.19× (z +9.2) | — |
| [[J82 (line)]] | alt | 113 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.56× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 25.4 | 2 | 0 | [[Triamcinolone (drug)]] 5 µM 2.97× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 41.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.3) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.72× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 66.5 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 6.73× (z +10.8) | — |
| [[C32 (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +11.1) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[CFPAC-1 (line)]] | alt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 53.3 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.48× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 71.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 37.8 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.76× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 32.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.295× (z -8.5) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SW48 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0985× (z -9.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1F]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[IRX3]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MT1M]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[ZFP36L1]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[DUSP1]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 465 |
| [[CCL20]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MT1E]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[IRS2]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MT1X]] | +0.63 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[ARRDC2]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SAA1]] | +0.63 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[MT2A]] | +0.63 | +0.56 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BANF1]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 457 |
| [[PGRMC1]] | -0.53 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[CDH6]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TMEM30A]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[BPNT2]] | -0.49 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[C2CD3]] | -0.48 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[AGO1]] | -0.48 | -0.39 / -0.52 | both halves | 5e-05 | pathway: Cellular Senescence |
| [[AP3M1]] | -0.48 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[FSTL1]] | -0.48 | -0.39 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHCG]] | B | RHCG activity raises CEBPB's level | lines that do not express RHCG (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without RHCG | 0.004 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[PTGES]] | B | PTGES activity raises CEBPB's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.91× lower at baseline in the lines without PTGES | 0.011 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[CCL20]] | B | CCL20 activity raises CEBPB's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.85× lower at baseline in the lines without CCL20 | 0.025 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[SAA1]] | B | SAA1 activity raises CEBPB's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 1.59× lower at baseline in the lines without SAA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11 |
| [[MAFB]] | B | MAFB activity raises CEBPB's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without MAFB | 0.068 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[ZC3H12A]] | B | ZC3H12A activity raises CEBPB's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 1.96× lower at baseline in the lines without ZC3H12A | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[C3]] | B | C3 activity raises CEBPB's level | lines that do not express C3 (32) vs lines expressing it (18) | 1.73× lower at baseline in the lines without C3 | 0.0997 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.2, 13.3); signed map (14.6, 29.9). **Vector** length 143, 49.3% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.50 to 11); *Metallothioneins bind metals* (reactome, mean cos +0.65 to 5); *metallothionein* (control, mean cos +0.65 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.2 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.6 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +7.1 | +4.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.3 | +5.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +5.2 | +4.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.1 | +4.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -9.9 | -1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -9.2 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -8.2 | -0.2 |
|  | [[NG25 (drug)]] 5 µM |  | -5.4 | -3.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.6 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CCAAT enhancer binding protein beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,190,830-50,192,668 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LAP, CRP2, NFIL6, IL6DBP, C/EBP-beta; previously TCF5 |
| Gene groups (HGNC) | CCAAT/enhancer binding proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, COMPLEMENT, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 18 pathways, smallest: Response of EIF2AK1 (HRI) to heme deficiency; ATF4 activates genes in response to endoplasmic reticulum  stress; Nuclear events stimulated by ALK signaling in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P17676](https://www.uniprot.org/uniprotkb/P17676) (CCAAT/enhancer-binding protein beta):

> Important transcription factor regulating the expression of genes involved in immune and inflammatory responses. Also plays a significant role in adipogenesis, as well as in the gluconeogenic pathway, liver regeneration, and hematopoiesis. The consensus recognition site is 5'-T[TG]NNGNAA[TG]-3'. Its functional capacity is governed by protein interactions and post-translational protein modifications. During early embryogenesis, plays essential and redundant roles with CEBPA. Has a promitotic …

**Summary**, from NCBI Gene [1051](https://www.ncbi.nlm.nih.gov/gene/1051):

> This intronless gene encodes a transcription factor that contains a basic leucine zipper (bZIP) domain. The encoded protein functions as a homodimer but can also form heterodimers with CCAAT/enhancer-binding proteins alpha, delta, and gamma. Activity of this protein is important in the regulation of genes involved in immune and inflammatory responses, among other processes. The use of alternative in-frame AUG start codons results in multiple protein isoforms, each with distinct biological …

**Accessions** — [HGNC:1834](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1834) · Entrez [1051](https://www.ncbi.nlm.nih.gov/gene/1051) · UniProt [P17676](https://www.uniprot.org/uniprotkb/P17676) · Ensembl [ENSG00000172216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172216)

## Data

Gene col 10225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10225); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10225]; `tensor/DDL_lfc|DDL_z.npy` [10225]; `embed/gene_vectors.npy` [10225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10225 or target_col == 10225). Every well: [[CEBPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEBPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
