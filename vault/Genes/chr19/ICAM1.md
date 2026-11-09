---
symbol: "ICAM1"
type: "gene"
col: 1618
ensembl_id: "ENSG00000090339"
name: "intercellular adhesion molecule 1"
location: "19p13.2"
module: 14
arm: "+"
pooled_cpm: 123.0
n_lines_expressing: 31
n_dd_up: 14
n_dd_down: 31
n_dd_up_clean: 12
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 12
direction_downstream: 15
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ICAM1

*intercellular adhesion molecule 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.16× (z +18.4, q 0e+00, up in 21 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.343× (z -12.1, q 5e-31, down in 28 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBIE]] (+0.63, fdr 1e-05), [[CD82]] (+0.63, fdr 7e-06), [[TNIP1]] (+0.61, fdr 7e-06); moves opposite to [[NCBP3]] (-0.47, fdr 5e-05), [[UBE2K]] (-0.47, fdr 5e-05), [[NCOA6]] (-0.44, fdr 6e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CXCL3]] → it (grade B ⚠); 15 go from it, the strongest it → [[CADM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.16×** | +18.4 | 0e+00 | 21/29 (Panc 03.27, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **15.2×** | +16.1 | 0e+00 | 29/30 (Panc 03.27, NCI-H2347, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +9.8 | 2e-20 | 20/30 (HepG2/C3A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.99×** | +9.5 | 3e-19 | 27/29 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.24×** | +8.7 | 3e-16 | 22/29 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.65×** | +5.7 | 1e-06 | 19/29 (SNU-423, HepG2/C3A, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.5 | 6e-04 | 14/29 (HEC-1-A, Hs 766T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.4 | 7e-04 | 15/29 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.47×** | +4.4 | 8e-04 | 17/29 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.001 | 18/29 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.007 | 19/30 (NCI-H1792, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.011 | 14/31 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.031 | 12/30 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bexarotene (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.071 | 12/29 (NCI-H1792, SK-MEL-2, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1618.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.343×** | -12.1 | 5e-31 | 28/29 (HCT15, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.665×** | -6.5 | 2e-08 | 21/29 (NCI-H23, NCI-H1792, …) | top dose only | low cells (technical?) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.670×** | -6.4 | 3e-08 | 25/30 (C32, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -5.9 | 5e-07 | 18/26 (SK-MEL-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.703×** | -5.6 | 2e-06 | 22/30 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.620×** | -5.4 | 5e-06 | 20/29 (NCI-H23, HCT15, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.620×** | -5.4 | 5e-06 | 20/29 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.614×** | -5.3 | 8e-06 | 21/30 (SK-MEL-2, SNU-423, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.635×** | -4.9 | 7e-05 | 19/29 (PANC-1, SW 900, …) | all doses, flat |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.652×** | -4.8 | 7e-05 | 21/29 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.463×** | -4.6 | 3e-04 | 20/29 (NCI-H23, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.664×** | -4.5 | 4e-04 | 19/28 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[NG25 (drug)]] 5 µM |  | **0.483×** | -4.3 | 7e-04 | 18/28 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.688×** | -4.2 | 9e-04 | 14/29 (NCI-H1792, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.688×** | -4.2 | 9e-04 | 18/29 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.780×** | -4.0 | 0.002 | 15/29 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.781×** | -4.0 | 0.002 | 13/29 (Panc 03.27, HEC-1-A, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.775×** | -3.9 | 0.003 | 17/30 (HCT15, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.716×** | -3.8 | 0.004 | 18/29 (HOP62, NCI-H1792, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 199 | 0 | 11 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.172× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 126 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +19.0) | [[Auranofin (drug)]] 5 µM 0.221× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 122 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +23.0) | [[Auranofin (drug)]] 5 µM 0.256× (z -10.8) |
| [[SW 900 (line)]] | alt | 91.4 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 28.5× (z +10.4) | [[Homoharringtonine (drug)]] 0.05 µM 0.177× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 177 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 15.2× (z +14.8) | — |
| [[PANC-1 (line)]] | alt | 293 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 18.0× (z +12.1) | [[Auranofin (drug)]] 5 µM 0.234× (z -11.5) |
| [[SNU-423 (line)]] | alt | 327 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 127 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 408 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.400× (z -10.0) |
| [[HCT15 (line)]] | alt | 169 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.148× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 524 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.402× (z -9.4) |
| [[A549 (line)]] | wt | 65.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +16.7) | — |
| [[CFPAC-1 (line)]] | alt | 115 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.6) | [[Auranofin (drug)]] 5 µM 0.199× (z -12.2) |
| [[HOP62 (line)]] | alt | 182 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 25.1× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 57.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 35.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +16.0) | — |
| [[J82 (line)]] | alt | 142 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +17.8) | — |
| [[A-427 (line)]] | wt | 116 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 14.3× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 186 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +15.6) | — |
| [[HS-578T (line)]] | alt | 242 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 144 | 1 | 1 (1 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.38× (z +8.6) | [[Selinexor (drug)]] 5 µM 0.405× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 482 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.5) | — |
| [[CHP-212 (line)]] | wt | 63.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 326 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.9× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 74.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +8.7) | — |
| [[A-172 (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 27.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.66 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIE]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 532 |
| [[CD82]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 626 |
| [[TNIP1]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IFNGR2]] | +0.59 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[GATM]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[CD274]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 757 |
| [[IL1A]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 807 |
| [[CD83]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 696 |
| [[IFNAR2]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[NFKB2]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 755 |
| [[NINJ1]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BCL2A1]] | +0.53 | +0.59 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 464 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP3]] | -0.47 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[UBE2K]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[NCOA6]] | -0.44 | -0.39 / -0.40 | both halves | 6e-05 | pathway: Affinity selection of immunoglobulins |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity strengthens ICAM1's drug response | lines that do not express CXCL3 (10) vs lines expressing it (20) | the lines without CXCL3 respond 0.55× as strongly (z diff +2.45); strongest at Homoharringtonine 5 µM: 1.03x vs 4.05x (z diff +8.5) | 0.002 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; target measured in part of the lines; artifact flags |
| [[CD74]] | B | CD74 activity raises ICAM1's level | lines that do not express CD74 (31) vs lines expressing it (19) | 3.00× lower at baseline in the lines without CD74 | 0.039 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[CADM1]] | B | CADM1 activity raises ICAM1's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 3.31× lower at baseline in the lines without CADM1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[VDR]] | B | VDR activity raises ICAM1's level | lines that do not express VDR (8) vs lines expressing it (42) | 3.89× lower at baseline in the lines without VDR | 0.081 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[CX3CL1]] | B | CX3CL1 activity raises ICAM1's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 3.02× lower at baseline in the lines without CX3CL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[NR3C1]] | B | NR3C1 activity lowers ICAM1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[HLA-A]] | B | HLA-A activity raises ICAM1's level | lines that do not express HLA-A (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without HLA-A | 0.089 | ⚠ within organs, on part of the lines; also absent: PHLDA1, S100A6, HLA-H; its own permutation p |
| [[GALNT18]] | B | GALNT18 activity raises ICAM1's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 2.59× lower at baseline in the lines without GALNT18 | 0.099 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[BCL2A1]] | C | BCL2A1 activity raises ICAM1's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.88× lower at baseline in the lines without BCL2A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; co-absent with the target |
| [[MIR3142HG]] | C | MIR3142HG activity raises ICAM1's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 3.87× lower at baseline in the lines without MIR3142HG | 0.024 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130; co-absent with the target |
| [[PINLYP]] | C | PINLYP activity raises ICAM1's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 2.87× lower at baseline in the lines without PINLYP | 0.063 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent; co-absent with the target |
| [[G0S2]] | C | G0S2 activity raises ICAM1's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without G0S2 | 0.086 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADM1]] | B | ICAM1 activity raises CADM1's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 4.05× lower at baseline in the lines without ICAM1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[NFKBIE]] | B | ICAM1 activity raises NFKBIE's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without ICAM1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[RARA]] | B | ICAM1 activity raises RARA's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without ICAM1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[LINC02605]] | B | ICAM1 activity raises LINC02605's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without ICAM1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[NAV2]] | B | ICAM1 activity raises NAV2's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 2.65× lower at baseline in the lines without ICAM1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[NOTCH2]] | B | ICAM1 activity raises NOTCH2's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without ICAM1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[GALNT18]] | B | ICAM1 activity raises GALNT18's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 2.28× lower at baseline in the lines without ICAM1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[HLA-A]] | B | ICAM1 activity raises HLA-A's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.49× lower at baseline in the lines without ICAM1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[IRAK2]] | B | ICAM1 activity raises IRAK2's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without ICAM1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[SLC9A7]] | B | ICAM1 activity raises SLC9A7's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without ICAM1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[TRAF1]] | B | ICAM1 activity raises TRAF1's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without ICAM1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[RNF24]] | B | ICAM1 activity raises RNF24's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.43× lower at baseline in the lines without ICAM1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.3, 2.6); signed map (43.1, 8.2). **Vector** length 118, 36.8% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +16.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +9.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[Fusidic acid (drug)]] 5 µM |  | +1.4 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.8 | -12.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.8 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.1 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -2.6 |
|  | [[NG25 (drug)]] 5 µM |  | -4.2 | -4.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.0 | -6.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.3 | -5.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | intercellular adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,271,093-10,286,615 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BB2, CD54 |
| Gene groups (HGNC) | CD molecules; Receptor ligands; Immunoglobulin like domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, UV_RESPONSE_UP, APICAL_JUNCTION, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: Interleukin-10 signaling; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Integrin cell surface interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P05362](https://www.uniprot.org/uniprotkb/P05362) (Intercellular adhesion molecule 1):

> Cell adhesion molecule that functions as a receptor ligand of the signaling receptor ITGAL:ITGB2/LFA-1 (lymphocyte-function associated (LFA) molecule 1) ensuring leukocyte cell-cell adhesion, by providing a calibrated system to namely adjust T-cell killing to the antigen stimulation strength. Also functions as a ligand receptor of the signaling receptor ITGAM:ITGB2/MAC-1 ensuring adhesion between stimulated neutrophils and stimulated endothelial cells. During leukocyte trans-endothelial …

**Summary**, from NCBI Gene [3383](https://www.ncbi.nlm.nih.gov/gene/3383):

> This gene encodes a cell surface glycoprotein which is typically expressed on endothelial cells and cells of the immune system. It binds to integrins of type CD11a / CD18, or CD11b / CD18 and is also exploited by Rhinovirus as a receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5344) · Entrez [3383](https://www.ncbi.nlm.nih.gov/gene/3383) · UniProt [P05362](https://www.uniprot.org/uniprotkb/P05362) · Ensembl [ENSG00000090339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090339)

## Data

Gene col 1618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1618); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1618]; `tensor/DDL_lfc|DDL_z.npy` [1618]; `embed/gene_vectors.npy` [1618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1618 or target_col == 1618). Every well: [[ICAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ICAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
