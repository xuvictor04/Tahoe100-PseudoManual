---
symbol: "CFH"
type: "gene"
col: 4
ensembl_id: "ENSG00000000971"
name: "complement factor H"
location: "1q31.3"
module: 70
arm: "+"
pooled_cpm: 15.98
n_lines_expressing: 22
n_dd_up: 30
n_dd_down: 17
n_dd_up_clean: 25
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 29
direction_downstream: 38
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# CFH

*complement factor H* — 1q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +12.8, q 2e-34, up in 16 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.658× (z -5.0, q 1e-04, down in 13 of 19 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 0.660× (z -5.0, q 1e-04, down in 10 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP1]] (+0.74, fdr 7e-06), [[KCNT2]] (+0.72, fdr 7e-06, ⚠ same locus), [[CFB]] (+0.72, fdr 7e-06), [[TRANK1]] (+0.70, fdr 7e-06); moves opposite to [[DIP2A]] (-0.60, fdr 1e-05), [[DPP9]] (-0.55, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[SLC16A4]] → it (grade B ⚠); 38 go from it, the strongest it → [[LINC02605]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +12.8 | 2e-34 | 16/20 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +11.9 | 3e-30 | 10/18 (HS-578T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +11.7 | 2e-29 | 4/20 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.95×** | +11.3 | 3e-27 | 15/20 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.18×** | +9.3 | 2e-18 | 13/19 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +7.9 | 2e-13 | 4/16 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +6.5 | 8e-09 | 13/20 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +5.8 | 4e-07 | 14/19 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.8 | 5e-07 | 10/19 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.5 | 2e-06 | 5/19 (SW 900, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +5.4 | 3e-06 | 4/13 (HT-29, SW 900, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 3e-05 | 14/19 (NCI-H2347, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +4.7 | 9e-05 | 13/19 (NCI-H2347, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.5 | 3e-04 | 6/19 (SW 900, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.48×** | +4.3 | 8e-04 | 13/20 (NCI-H2347, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 9/20 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 10/20 (HOP62, SW 900, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 13/20 (NCI-H2347, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.003 | 14/20 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.005 | 4/19 (NCI-H2347, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.658×** | -5.0 | 1e-04 | 13/19 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.660×** | -5.0 | 1e-04 | 10/19 (SNU-1, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.661×** | -5.0 | 1e-04 | 12/19 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -4.9 | 2e-04 | 13/19 (A549, HT-29, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.753×** | -4.8 | 2e-04 | 15/20 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.779×** | -4.2 | 0.002 | 12/20 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.709×** | -4.1 | 0.003 | 8/19 (CFPAC-1, SW 900, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -3.8 | 0.011 | 14/19 (HT-29, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.013 | 13/19 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.727×** | -3.7 | 0.013 | 6/20 (A549, CFPAC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.756×** | -3.3 | 0.042 | 9/19 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.760×** | -3.3 | 0.048 | 11/19 (NCI-H1792, NCI-H2347, …) | all doses, flat |  |
| [[Tofacitinib (citrate) (drug)]] 0.05 µM |  | **0.762×** | -3.3 | 0.048 | 6/19 (NCI-H2347, Hs 766T, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.765×** | -3.2 | 0.050 | 14/19 (SW 900, SNU-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.766×** | -3.2 | 0.050 | 5/19 (SK-MEL-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.767×** | -3.2 | 0.050 | 10/19 (SNU-1, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.770×** | -3.0 | 0.085 | 5/19 (NCI-H1792, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 85.9 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 42.8 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.96× (z +13.7) | [[Vinblastine (sulfate) (drug)]] 5 µM 0.190× (z -10.5) |
| [[HS-578T (line)]] | alt | 25.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +14.8) | — |
| [[hTERT-HPNE (line)]] | wt | 50.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +22.5) | — |
| [[SNU-1 (line)]] | wt | 150 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.159× (z -10.9) |
| [[HOP62 (line)]] | alt | 9.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +18.6) | — |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.142× (z -9.5) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.191× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 97.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.312× (z -9.5) ⚠ unreliable plate only · without an alert: [[Tofacitinib (drug)]] 5 µM 0.452× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 35.1 | 2 | 0 | [[Cobimetinib (drug)]] 5 µM 5.40× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +10.9) | — |
| [[A498 (line)]] | wt | 92.1 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.466× (z -8.6) |
| [[A549 (line)]] | wt | 8.74 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0661× (z -8.6) |
| [[A-172 (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.26 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP1]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[KCNT2]] | +0.72 | +0.67 / +0.65 | both halves | 7e-06 | ⚠ same locus (42.5 kb: neighbours can correlate without regulation) |
| [[CFB]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_COAGULATION; STRING 961 |
| [[TRANK1]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[LUM]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[KYNU]] | +0.67 | +0.62 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[GBP2]] | +0.67 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[TLR3]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TNFAIP6]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SLFN12]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[RARRES1]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[IFIT2]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[NCOA7]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[DPP9]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 10, C 19. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A4]] | B | SLC16A4 activity raises CFH's level | lines that do not express SLC16A4 (15) vs lines expressing it (35) | 3.68× lower at baseline in the lines without SLC16A4 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNFRSF10C, LYPD3, GNAS-AS1; maybe low, not absent |
| [[TLR3]] | B | TLR3 activity raises CFH's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 3.11× lower at baseline in the lines without TLR3 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CFH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TRIM22]] | B | TRIM22 activity raises CFH's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.45× lower at baseline in the lines without TRIM22 | 0.049 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[LINC02605]] | B | LINC02605 activity raises CFH's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 2.50× lower at baseline in the lines without LINC02605 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises CFH's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.07× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.061 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[CASP10]] | B | CASP10 activity raises CFH's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without CASP10 | 0.070 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[IFIT3]] | B | IFIT3 activity raises CFH's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 3.65× lower at baseline in the lines without IFIT3 | 0.075 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[CTSS]] | B | CTSS activity raises CFH's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.19× lower at baseline in the lines without CTSS | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[IFIT2]] | B | IFIT2 activity raises CFH's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 3.57× lower at baseline in the lines without IFIT2 | 0.095 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[LINC02057]] | C | LINC02057 activity raises CFH's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 3.52× lower at baseline in the lines without LINC02057 | 0.004 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6; co-absent with the target |
| [[FYB1]] | C | FYB1 activity raises CFH's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.77× lower at baseline in the lines without FYB1 | 0.005 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 20, C 18. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02605]] | B | CFH activity raises LINC02605's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without CFH | 0.018 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[SLC16A4]] | B | CFH activity raises SLC16A4's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without CFH | 0.023 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[FNDC3B]] | B | CFH activity raises FNDC3B's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.71× lower at baseline in the lines without CFH | 0.027 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[GBP1]] | B | CFH activity raises GBP1's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without CFH | 0.029 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[B2M]] | B | CFH activity raises B2M's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.70× lower at baseline in the lines without CFH | 0.030 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[STAT4]] | B | CFH activity raises STAT4's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without CFH | 0.030 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[CTSO]] | B | CFH activity raises CTSO's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without CFH | 0.032 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[CTSS]] | B | CFH activity raises CTSS's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.29× lower at baseline in the lines without CFH | 0.039 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[CFB]] | B | CFH activity raises CFB's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without CFH | 0.042 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[SPTLC3]] | B | CFH activity raises SPTLC3's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.75× lower at baseline in the lines without CFH | 0.042 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[IFI44L]] | B | CFH activity raises IFI44L's level | lines that do not express CFH (28) vs lines expressing it (22) | 3.79× lower at baseline in the lines without CFH | 0.057 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[SAMD9L]] | B | CFH activity raises SAMD9L's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.97× lower at baseline in the lines without CFH | 0.057 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.4, 23.6); signed map (47.0, 24.9). **Vector** length 74.4, 22.7% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.52 to 13); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.51 to 9); *allograft rejection* (hallmark, mean cos +0.53 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +11.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +4.3 |
| fall | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.7 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | complement factor H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.3 — chr1:196,651,754-196,752,476 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUS, FHL1, ARMS1, ARMD4; previously HF, HF1, HF2 |
| Gene groups (HGNC) | Sushi domain containing; Complement system regulators and receptors |
| Hallmark sets | COAGULATION, COMPLEMENT, KRAS_SIGNALING_UP, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Regulation of Complement cascade; Complement cascade; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P08603](https://www.uniprot.org/uniprotkb/P08603) (Complement factor H):

> Glycoprotein that plays an essential role in maintaining a well-balanced immune response by modulating complement activation. Acts as a soluble inhibitor of complement, where its binding to self markers such as glycan structures prevents complement activation and amplification on cell surfaces. Accelerates the decay of the complement alternative pathway (AP) C3 convertase C3bBb, thus preventing local formation of more C3b, the central player of the complement amplification loop. As a cofactor …

**Summary**, from NCBI Gene [3075](https://www.ncbi.nlm.nih.gov/gene/3075):

> This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-uremic syndrome (HUS) and chronic hypocomplementemic nephropathy. Alternate transcriptional splice …

**Accessions** — [HGNC:4883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4883) · Entrez [3075](https://www.ncbi.nlm.nih.gov/gene/3075) · UniProt [P08603](https://www.uniprot.org/uniprotkb/P08603) · Ensembl [ENSG00000000971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000000971)

## Data

Gene col 4: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4]; `tensor/DDL_lfc|DDL_z.npy` [4]; `embed/gene_vectors.npy` [4]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4 or target_col == 4). Every well: [[CFH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
