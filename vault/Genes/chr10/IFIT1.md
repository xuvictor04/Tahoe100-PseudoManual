---
symbol: "IFIT1"
type: "gene"
col: 11726
ensembl_id: "ENSG00000185745"
name: "interferon induced protein with tetratricopeptide repeats 1"
location: "10q23.31"
module: 32
arm: "+"
pooled_cpm: 53.2
n_lines_expressing: 46
n_dd_up: 29
n_dd_down: 58
n_dd_up_clean: 29
n_dd_down_clean: 48
in_vector_space: true
direction_upstream: 62
direction_downstream: 39
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFIT1

*interferon induced protein with tetratricopeptide repeats 1* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.64× (z +7.3, q 2e-10, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 58 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.194× (z -12.2, q 1e-31, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT3]] (+0.96, fdr 7e-06, ⚠ same locus), [[PARP9]] (+0.94, fdr 7e-06), [[OAS2]] (+0.94, fdr 7e-06), [[CMPK2]] (+0.93, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 62 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 39 go from it, the strongest it → [[RIGI]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, none with an alert; shown: the 15 strongest. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.64×** | +7.3 | 2e-10 | 32/43 (NCI-H460, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.60×** | +6.9 | 2e-09 | 37/43 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **2.09×** | +5.5 | 6e-06 | 31/43 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.75×** | +5.1 | 5e-05 | 28/44 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.57×** | +5.0 | 7e-05 | 24/45 (NCI-H460, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.93×** | +4.7 | 2e-04 | 31/43 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.86×** | +4.7 | 2e-04 | 28/45 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.92×** | +4.6 | 3e-04 | 32/45 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.66×** | +4.6 | 3e-04 | 29/44 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.54×** | +4.6 | 3e-04 | 26/44 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.64×** | +4.4 | 6e-04 | 26/45 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.47×** | +4.0 | 0.003 | 25/45 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.75×** | +4.0 | 0.003 | 25/44 (CFPAC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.69×** | +4.0 | 0.003 | 26/45 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.69×** | +3.9 | 0.003 | 28/44 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 58 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.194×** | -12.2 | 1e-31 | 39/44 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.327×** | -11.8 | 2e-29 | 36/45 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.387×** | -10.0 | 4e-21 | 36/44 (NCI-H1792, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.267×** | -9.8 | 1e-20 | 39/44 (C-33 A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.267×** | -9.8 | 1e-20 | 34/45 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.408×** | -9.4 | 4e-19 | 32/45 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.308×** | -8.8 | 1e-16 | 37/44 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.289×** | -8.7 | 2e-16 | 34/44 (NCI-H1792, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.344×** | -7.9 | 1e-13 | 32/44 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.352×** | -7.8 | 4e-13 | 29/45 (BT-474, C-33 A, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.352×** | -7.8 | 4e-13 | 33/44 (BT-474, SNU-423, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.352×** | -7.5 | 3e-12 | 30/42 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.495×** | -7.4 | 6e-12 | 37/45 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.375×** | -7.3 | 1e-11 | 35/44 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.376×** | -7.3 | 1e-11 | 31/44 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.379×** | -7.2 | 2e-11 | 29/43 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 131 | 0 | 21 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0778× (z -18.0) |
| [[BT-474 (line)]] | alt | 61.2 | 0 | 19 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -16.7) |
| [[RKO (line)]] | wt | 49.2 | 0 | 19 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0620× (z -11.4) |
| [[A549 (line)]] | wt | 69.2 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0567× (z -18.0) |
| [[NCI-H1792 (line)]] | alt | 50.4 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 42.0 | 0 | 14 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0803× (z -16.7) |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 14 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.101× (z -13.4) |
| [[A498 (line)]] | wt | 74.7 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -14.3) |
| [[C-33 A (line)]] | alt | 76.6 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.0487× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 141 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0247× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.103× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 131 | 1 | 8 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 4.97× (z +8.5) | [[Tofacitinib (drug)]] 5 µM 0.136× (z -15.4) |
| [[COLO 205 (line)]] | alt | 122 | 0 | 9 | — | [[Auranofin (drug)]] 5 µM 0.0546× (z -12.9) |
| [[LoVo (line)]] | wt | 38.6 | 0 | 9 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.146× (z -13.0) |
| [[HS-578T (line)]] | alt | 38.7 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 102 | 1 | 6 | [[Harringtonine (drug)]] 0.5 µM 4.72× (z +8.9) | [[Tofacitinib (drug)]] 5 µM 0.175× (z -14.1) |
| [[LS 180 (line)]] | wt | 51.2 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +12.4) | [[Auranofin (drug)]] 5 µM 0.182× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 35.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 84.7 | 5 | 0 | [[Harringtonine (drug)]] 0.5 µM 7.09× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +13.9) | — |
| [[SHP-77 (line)]] | alt | 25.1 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.186× (z -9.9) |
| [[A-172 (line)]] | wt | 163 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0779× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 27.6 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.101× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 29.4 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +12.9) | [[Selinexor (drug)]] 5 µM 0.262× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 28.6 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0517× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0261× (z -10.4) |
| [[Hs 766T (line)]] | wt | 127 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.234× (z -9.1) |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0443× (z -11.1) |
| [[SW1417 (line)]] | alt | 46.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.200× (z -8.7) |
| [[C32 (line)]] | wt | 23.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0276× (z -13.1) |
| [[CHP-212 (line)]] | wt | 46.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0559× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 84.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.182× (z -8.8) |
| [[PANC-1 (line)]] | alt | 18.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.157× (z -8.6) |
| [[A-427 (line)]] | wt | 6.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.50 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT3]] | +0.96 | +0.94 / +0.97 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999; ⚠ same locus (15.1 kb, same strand: neighbours can correlate without regulation) |
| [[PARP9]] | +0.94 | +0.90 / +0.94 | both halves | 7e-06 | STRING 751 |
| [[OAS2]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 966 |
| [[CMPK2]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 830 |
| [[MX1]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 989 |
| [[RSAD2]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 970 |
| [[RIGI]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 995 |
| [[IFIT2]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 982 |
| [[OAS1]] | +0.92 | +0.86 / +0.94 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 960 |
| [[IFIH1]] | +0.92 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 982 |
| [[IFI44]] | +0.92 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 974 |
| [[USP18]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 949 |
| [[OAS3]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 965 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 34, C 28. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises IFIT1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.70× lower at baseline in the lines without OAS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[RSAD2]] | B | RSAD2 activity raises IFIT1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.51× lower at baseline in the lines without RSAD2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[DDX60L]] | B | DDX60L activity raises IFIT1's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 3.49× lower at baseline in the lines without DDX60L | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[PLAAT4]] | B | PLAAT4 activity raises IFIT1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without PLAAT4 | 0.005 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[OASL]] | B | OASL activity raises IFIT1's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.98× lower at baseline in the lines without OASL | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[IFIT3]] | B | IFIT3 activity raises IFIT1's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 2.53× lower at baseline in the lines without IFIT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises IFIT1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.50× lower at baseline in the lines without OAS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises IFIT1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.30× lower at baseline in the lines without IFI44 | 0.009 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[SAMD9]] | B | SAMD9 activity raises IFIT1's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.50× lower at baseline in the lines without SAMD9 | 0.012 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[CASP10]] | B | CASP10 activity raises IFIT1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without CASP10 | 0.014 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[LMO2]] | B | LMO2 activity raises IFIT1's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 2.00× lower at baseline in the lines without LMO2 | 0.015 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[TRANK1]] | B | TRANK1 activity raises IFIT1's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.44× lower at baseline in the lines without TRANK1 | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 0, C 39. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIGI]] | C | IFIT1 activity raises RIGI's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 4.05× lower at baseline in the lines without IFIT1 | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[IFI44]] | C | IFIT1 activity raises IFI44's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 6.51× lower at baseline in the lines without IFIT1 | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[ZC3HAV1]] | C | IFIT1 activity raises ZC3HAV1's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without IFIT1 | 0.006 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[ISG15]] | C | IFIT1 activity raises ISG15's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 3.22× lower at baseline in the lines without IFIT1 | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[TRANK1]] | C | IFIT1 activity raises TRANK1's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 3.74× lower at baseline in the lines without IFIT1 | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[NMI]] | C | IFIT1 activity strengthens NMI's drug response | lines that do not express IFIT1 (4) vs lines expressing it (40) | the lines without IFIT1 respond 0.62× as strongly (z diff +2.56); strongest at Homoharringtonine 5 µM: 0.94x vs 0.57x (z diff +3.5) | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188; target measured in part of the lines; artifact flags |
| [[DDX60L]] | C | IFIT1 activity raises DDX60L's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 5.54× lower at baseline in the lines without IFIT1 | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[IFIT3]] | C | IFIT1 activity raises IFIT3's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 5.57× lower at baseline in the lines without IFIT1 | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[NCOA7]] | C | IFIT1 activity raises NCOA7's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without IFIT1 | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[OAS1]] | C | IFIT1 activity raises OAS1's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 5.35× lower at baseline in the lines without IFIT1 | 0.027 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[SAMD9]] | C | IFIT1 activity raises SAMD9's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 5.64× lower at baseline in the lines without IFIT1 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |
| [[OASL]] | C | IFIT1 activity raises OASL's level | lines that do not express IFIT1 (4) vs lines expressing it (46) | 4.02× lower at baseline in the lines without IFIT1 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OAS3, SP110, ENSG00000287188 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.950). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.5, 53.7); signed map (64.8, 31.7). **Vector** length 161, 62.9% of its response variance represented; |z| ≥ 3 in 1,867 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.80 to 56); *Interferon gamma signaling* (reactome, mean cos +0.78 to 17); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.84 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.3 | +7.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.6 | -0.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.7 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.4 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.8 | +6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.8 | +5.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -11.2 | -11.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -10.3 | -9.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -9.9 | -7.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.5 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.1 | -10.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.7 | -9.8 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced protein with tetratricopeptide repeats 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:89,392,546-89,406,487 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GARG-16, ISG56; previously G10P1, IFI56, IFNAI1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 7 pathways, smallest: Viral strategies to evade IFIT action; IFIT antiviral response; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P09914](https://www.uniprot.org/uniprotkb/P09914) (Antiviral innate immune response effector IFIT1):

> Plays a key role in the innate immune response as part of an interferon-dependent multiprotein complex, recognizing and sequestering viral RNAs that lack host-specific 2'-O-methylation at their 5' cap. By distinguishing these RNAs from host mRNAs, inhibits their translation by competing with the translation initiation factor eIF4E. Could also prevent viral replication through its interaction with DNA replication origin-binding protein E1 of several viruses. Causes the translocation of E1 from …

**Summary**, from NCBI Gene [3434](https://www.ncbi.nlm.nih.gov/gene/3434):

> This gene encodes a protein containing tetratricopeptide repeats that was originally identified as induced upon treatment with interferon. The encoded protein may inhibit viral replication and translational initiation. This gene is located in a cluster on chromosome 10 with five other closely related genes. There is a pseudogene for this gene on chromosome 13. Alternatively spliced transcript variants encoding multiple isoforms have been observed. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:5407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5407) · Entrez [3434](https://www.ncbi.nlm.nih.gov/gene/3434) · UniProt [P09914](https://www.uniprot.org/uniprotkb/P09914) · Ensembl [ENSG00000185745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185745)

## Data

Gene col 11726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11726); `tables/drug_effects.parquet` (87 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11726]; `tensor/DDL_lfc|DDL_z.npy` [11726]; `embed/gene_vectors.npy` [11726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11726 or target_col == 11726). Every well: [[IFIT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFIT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
