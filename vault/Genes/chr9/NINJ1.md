---
symbol: "NINJ1"
type: "gene"
col: 5232
ensembl_id: "ENSG00000131669"
name: "ninjurin 1"
location: "9q22.31"
module: 14
arm: "+"
pooled_cpm: 21.03
n_lines_expressing: 45
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 16
direction_downstream: 7
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NINJ1

*ninjurin 1* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.71× (z +13.3, q 2e-37, up in 37 of 42 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.95× (z +9.8, q 3e-20, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.558× (z -5.5, q 2e-05, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEURL3]] (+0.79, fdr 7e-06), [[CCL5]] (+0.70, fdr 7e-06), [[NFKBIE]] (+0.68, fdr 7e-06); moves opposite to [[ZNF731P]] (-0.56, fdr 1e-05), [[ATP2A2]] (-0.54, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TNFAIP6]] → it (grade B ⚠); 7 go from it, the strongest it → [[CADM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.71×** | +13.3 | 2e-37 | 37/42 (HEC-1-A, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.95×** | +9.8 | 3e-20 | 38/42 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.26×** | +7.6 | 4e-12 | 27/42 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.71×** | +5.0 | 7e-05 | 22/40 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +4.9 | 9e-05 | 26/43 (NCI-H2347, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.49×** | +3.7 | 0.018 | 21/40 (A-172, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.45×** | +3.5 | 0.035 | 18/41 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.4 | 0.050 | 17/38 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.056 | 17/42 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.062 | 13/42 (RKO, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.078 | 12/42 (SNU-423, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.558×** | -5.5 | 2e-05 | 25/43 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -5.0 | 2e-04 | 25/42 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.631×** | -4.4 | 0.002 | 19/42 (C32, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -4.0 | 0.010 | 17/27 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.748×** | -3.9 | 0.011 | 18/42 (Hs 766T, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.676×** | -3.7 | 0.020 | 20/43 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.699×** | -3.4 | 0.051 | 17/41 (HS-578T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -3.4 | 0.051 | 12/43 (A549, SK-MEL-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.702×** | -3.3 | 0.051 | 15/43 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 0.728× | -3.0 | 0.15 | 13/43 (HS-578T, NCI-H1792, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 10.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.0× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 7.78 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.5× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -11.0) |
| [[A498 (line)]] | wt | 81.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +11.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.46× (z +8.6) | — |
| [[C32 (line)]] | wt | 25.4 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 4.59× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.205× (z -9.0) |
| [[HOP62 (line)]] | alt | 17.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.03× (z +9.6) | — |
| [[J82 (line)]] | alt | 37.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.16× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 21.3 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.68× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SHP-77 (line)]] | alt | 7.06 | 0 | 2 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0777× (z -9.9) |
| [[SNU-423 (line)]] | alt | 57.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.64× (z +9.8) | — |
| [[A-172 (line)]] | wt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 9.67 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +15.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +11.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HepG2_C3A (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 45.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 42.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0446× (z -16.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEURL3]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[CCL5]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKBIE]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SLC2A6]] | +0.68 | +0.57 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[LACTB]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[C15orf48]] | +0.66 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[STARD10]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ADORA2A]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.62 | +0.66 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[RILP]] | +0.62 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[PIK3IP1]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[IL1A]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ATP2A2]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFAIP6]] | B | TNFAIP6 activity raises NINJ1's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.87× lower at baseline in the lines without TNFAIP6 | 3e-04 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[ENTHD1]] | B | ENTHD1 activity raises NINJ1's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.36× lower at baseline in the lines without ENTHD1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[SSTR2]] | B | SSTR2 activity raises NINJ1's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without SSTR2 | 0.006 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[IL32]] | B | IL32 activity raises NINJ1's level | lines that do not express IL32 (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without IL32 | 0.008 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[CSF2]] | B | CSF2 activity raises NINJ1's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without CSF2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[TNFRSF9]] | B | TNFRSF9 activity raises NINJ1's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without TNFRSF9 | 0.024 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[RRAD]] | B | RRAD activity raises NINJ1's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without RRAD | 0.028 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[G0S2]] | B | G0S2 activity raises NINJ1's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.18× lower at baseline in the lines without G0S2 | 0.031 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[STAT5A]] | B | STAT5A activity raises NINJ1's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.72× lower at baseline in the lines without STAT5A | 0.042 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[NEURL3]] | B | NEURL3 activity raises NINJ1's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.15× lower at baseline in the lines without NEURL3 | 0.050 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[NOD2]] | B | NOD2 activity raises NINJ1's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.80× lower at baseline in the lines without NOD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[TRAF1]] | B | TRAF1 activity raises NINJ1's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.07× lower at baseline in the lines without TRAF1 | 0.073 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADM1]] | B | NINJ1 activity raises CADM1's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 3.42× lower at baseline in the lines without NINJ1 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[STAT5A]] | B | NINJ1 activity raises STAT5A's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without NINJ1 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[TNFRSF9]] | B | NINJ1 activity raises TNFRSF9's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 2.98× lower at baseline in the lines without NINJ1 | 0.052 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[LINC01273]] | B | NINJ1 activity lowers LINC01273's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 1.93× higher at baseline in the lines without NINJ1 | 0.059 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[BHLHE40]] | B | NINJ1 activity raises BHLHE40's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without NINJ1 | 0.078 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[PIM2]] | B | NINJ1 activity raises PIM2's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without NINJ1 | 0.086 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[TMEM63B]] | B | NINJ1 activity strengthens TMEM63B's drug response | lines that do not express NINJ1 (5) vs lines expressing it (43) | the lines without NINJ1 respond 0.58× as strongly (z diff +0.68); strongest at Homoharringtonine 5 µM: 0.41x vs 1.48x (z diff +10.8) | 0.093 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, 2.3); signed map (43.7, 10.0). **Vector** length 108, 30.7% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.51 to 12); *inflammatory response* (hallmark, mean cos +0.52 to 22); *IL6 JAK STAT3 signaling* (hallmark, mean cos +0.50 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.3 | +13.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.3 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ninjurin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:93,121,496-93,134,251 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NIN1 |
| Hallmark sets | XENOBIOTIC_METABOLISM, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92982](https://www.uniprot.org/uniprotkb/Q92982) (Ninjurin-1):

> [Ninjurin-1]: Effector of various programmed cell death, such as pyroptosis and toxin-induced necrosis, which mediates plasma membrane rupture (cytolysis). Oligomerizes in response to death stimuli and forms ring-like structures on the plasma membrane: acts by cutting and shedding membrane disks, like a cookie cutter, leading to membrane damage and loss that cannot be repaired by the cell. Plasma membrane rupture leads to release intracellular molecules named damage-associated molecular …

**Summary**, from NCBI Gene [4814](https://www.ncbi.nlm.nih.gov/gene/4814):

> The ninjurin protein is upregulated after nerve injury both in dorsal root ganglion neurons and in Schwann cells (Araki and Milbrandt, 1996 [PubMed 8780658]). It demonstrates properties of a homophilic adhesion molecule and promotes neurite outgrowth from primary cultured dorsal root ganglion neurons.[supplied by OMIM, Aug 2009]

**Accessions** — [HGNC:7824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7824) · Entrez [4814](https://www.ncbi.nlm.nih.gov/gene/4814) · UniProt [Q92982](https://www.uniprot.org/uniprotkb/Q92982) · Ensembl [ENSG00000131669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131669)

## Data

Gene col 5232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5232); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5232]; `tensor/DDL_lfc|DDL_z.npy` [5232]; `embed/gene_vectors.npy` [5232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5232 or target_col == 5232). Every well: [[NINJ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NINJ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
