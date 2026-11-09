---
symbol: "SOCS3"
type: "gene"
col: 11550
ensembl_id: "ENSG00000184557"
name: "suppressor of cytokine signaling 3"
location: "17q25.3"
module: 14
arm: "+"
pooled_cpm: 19.4
n_lines_expressing: 44
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SOCS3

*suppressor of cytokine signaling 3* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +9.6, q 6e-19, up in 23 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (none with an alert); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.540× (z -9.9, q 2e-20, down in 34 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SBNO2]] (+0.73, fdr 7e-06), [[ZC3H12A]] (+0.72, fdr 7e-06), [[ZFP36]] (+0.69, fdr 7e-06); moves opposite to [[NAP1L4]] (-0.56, fdr 3e-05), [[SNX4]] (-0.53, fdr 3e-05), [[ASB7]] (-0.53, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ETS2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PLEKHO2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +9.6 | 6e-19 | 23/40 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +7.8 | 2e-12 | 24/41 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +6.5 | 2e-08 | 23/41 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.2 | 9e-08 | 28/42 (A-172, C32, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +6.1 | 1e-07 | 25/40 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +4.1 | 0.004 | 11/28 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.008 | 16/42 (NCI-H2030, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.6 | 0.021 | 13/37 (CFPAC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.028 | 19/41 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.540×** | -9.9 | 2e-20 | 34/42 (C32, SHP-77, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.551×** | -9.6 | 2e-19 | 27/42 (NCI-H23, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.573×** | -9.0 | 5e-17 | 37/42 (C32, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.495×** | -8.0 | 2e-13 | 33/41 (HT-29, A498, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.531×** | -6.9 | 4e-10 | 27/40 (A498, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -6.2 | 4e-08 | 26/39 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[NG25 (drug)]] 5 µM |  | **0.356×** | -6.1 | 6e-08 | 26/36 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -5.7 | 8e-07 | 22/40 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -5.7 | 8e-07 | 24/39 (hTERT-HPNE, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -5.6 | 1e-06 | 22/40 (HT-29, NCI-H1792, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.630×** | -5.3 | 7e-06 | 24/42 (SNU-423, HS-578T, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.637×** | -5.1 | 1e-05 | 23/42 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.461×** | -4.6 | 2e-04 | 22/36 (SHP-77, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.668×** | -4.6 | 2e-04 | 21/42 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.678×** | -4.4 | 4e-04 | 24/41 (NCI-H1792, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 60.7 | 14 (6 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 14.5× (z +20.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -12.9) |
| [[A498 (line)]] | wt | 22.6 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.258× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 53.7 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +24.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.5) |
| [[A549 (line)]] | wt | 29.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +13.2) | — |
| [[RKO (line)]] | wt | 19.2 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0540× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0808× (z -10.7) |
| [[C32 (line)]] | wt | 21.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | [[Tofacitinib (drug)]] 5 µM 0.0512× (z -20.8) |
| [[HOP62 (line)]] | alt | 22.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +15.0) | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.174× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 36.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +11.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 23.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +13.6) | [[Tofacitinib (drug)]] 5 µM 0.276× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 38.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -8.9) |
| [[HS-578T (line)]] | alt | 16.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 8.80× (z +9.6) | — |
| [[A-427 (line)]] | wt | 17.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.139× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 8.41 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.198× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.161× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[PANC-1 (line)]] | alt | 22.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.157× (z -10.4) |
| [[A-172 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBNO2]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 | STRING 469 |
| [[ZC3H12A]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ZFP36]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 565 |
| [[JUNB]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 623 |
| [[CSRNP1]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 | STRING 513 |
| [[TRIB1]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TNKS1BP1]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[HELZ2]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[C3]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[NFKBIZ]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 | STRING 626 |
| [[BCL3]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 666 |
| [[FOSL2]] | +0.59 | +0.64 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 487 |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAP1L4]] | -0.56 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[SNX4]] | -0.53 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[ASB7]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PPHLN1]] | -0.53 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[TRPC4AP]] | -0.52 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[BMPR1A]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[KLHDC10]] | -0.51 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[GAPVD1]] | -0.51 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[FHIP2A]] | -0.51 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[TNPO3]] | -0.51 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[RAB18]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[LINC03006-1]] | -0.50 | -0.34 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETS2]] | B | ETS2 activity raises SOCS3's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without ETS2 | 0.082 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SOCS3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[IFI16]] | B | IFI16 activity raises SOCS3's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without IFI16 | 0.094 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHO2]] | B | SOCS3 activity raises PLEKHO2's level | lines that do not express SOCS3 (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without SOCS3 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with PIK3CA, ZFHX3, ACVR2A; also absent: LARP6, PTPRH, ZNF284; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.472). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.5, 8.1); signed map (11.0, 28.6). **Vector** length 110, 26.4% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +9.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.6 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.5 | -9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -8.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.5 | -9.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -5.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.6 | -9.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.4 | -5.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.3 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | suppressor of cytokine signaling 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,356,778-78,360,077 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SSI-3, CIS3, SOCS-3, Cish3 |
| Gene groups (HGNC) | SH2 domain containing; Suppressors of cytokine signaling |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 24 pathways, smallest: PTK6 Activates STAT3; RUNX1 regulates transcription of genes involved in differentiation of keratinocytes; Signaling by Leptin |
| Matched by | ensembl_id |

**Function**, from UniProt [O14543](https://www.uniprot.org/uniprotkb/O14543) (Suppressor of cytokine signaling 3):

> SOCS family proteins form part of a classical negative feedback system that regulates cytokine signal transduction. SOCS3 is involved in negative regulation of cytokines that signal through the JAK/STAT pathway. Inhibits signal transduction by binding to transmembrane signaling receptors including IL6ST/gp130, LIFR, EPOR, INSR, IL12RB2, CSF3R/G-CSF-R and LEPR. Binding to JAK2 inhibits its kinase activity and regulates IL6 signaling. Suppresses fetal liver erythropoiesis. Regulates onset and …

**Summary**, from NCBI Gene [9021](https://www.ncbi.nlm.nih.gov/gene/9021):

> This gene encodes a member of the STAT-induced STAT inhibitor (SSI), also known as suppressor of cytokine signaling (SOCS), family. SSI family members are cytokine-inducible negative regulators of cytokine signaling. The expression of this gene is induced by various cytokines, including IL6, IL10, and interferon (IFN)-gamma. The protein encoded by this gene can bind to JAK2 kinase, and inhibit the activity of JAK2 kinase. Studies of the mouse counterpart of this gene suggested the roles of this …

**Accessions** — [HGNC:19391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19391) · Entrez [9021](https://www.ncbi.nlm.nih.gov/gene/9021) · UniProt [O14543](https://www.uniprot.org/uniprotkb/O14543) · Ensembl [ENSG00000184557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184557)

## Data

Gene col 11550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11550); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11550]; `tensor/DDL_lfc|DDL_z.npy` [11550]; `embed/gene_vectors.npy` [11550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11550 or target_col == 11550). Every well: [[SOCS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOCS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
