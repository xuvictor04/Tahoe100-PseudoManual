---
symbol: "GBP5"
type: "gene"
col: 7807
ensembl_id: "ENSG00000154451"
name: "guanylate binding protein 5"
location: "1p22.2"
module: 32
arm: "+"
pooled_cpm: 2.08
n_lines_expressing: 26
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 18
direction_downstream: 56
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# GBP5

*guanylate binding protein 5* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.35× (z +21.2, q 0e+00, up in 14 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.625× (z -4.5, q 0.004, down in 16 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFI16]] (+0.80, fdr 7e-06), [[SAMD9L]] (+0.79, fdr 7e-06), [[XAF1]] (+0.77, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[OASL]] → it (grade B ⚠); 56 go from it, the strongest it → [[IKBKE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7807.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.35×** | +21.2 | 0e+00 | 14/16 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **8.98×** | +14.7 | 0e+00 | 14/15 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.94×** | +11.5 | 2e-28 | 14/17 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.81×** | +10.1 | 5e-22 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.49×** | +8.4 | 5e-15 | 14/20 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.38×** | +7.6 | 4e-12 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +7.4 | 1e-11 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.40×** | +5.9 | 3e-07 | 13/17 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.6 | 2e-06 | 0/16 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.84×** | +5.0 | 3e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +4.9 | 4e-05 | 7/20 (SW1417, Hs 766T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +4.7 | 1e-04 | 2/5 (HS-578T, SNU-423) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.73×** | +3.7 | 0.010 | 1/10 (NCI-H1792) | inconsistent across doses | low cells (technical?); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.11×** | +3.6 | 0.014 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.73×** | +3.5 | 0.016 | 5/15 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Orlistat (drug)]] 0.05 µM |  | **1.71×** | +3.3 | 0.031 | 0/11 | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.041 | 1/20 (LOX-IMVI) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.65×** | +3.1 | 0.055 | 1/10 (Panc 03.27) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.62×** | +3.1 | 0.055 | 1/10 (Hs 766T) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.57×** | +3.0 | 0.061 | 4/20 (HS-578T, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7807.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.625×** | -4.5 | 0.004 | 16/19 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.672×** | -3.8 | 0.033 | 10/20 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.579×** | -3.7 | 0.033 | 11/21 (SNU-423, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -3.7 | 0.033 | 12/19 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rucaparib (phosphate) (drug)]] 0.05 µM |  | **0.573×** | -3.5 | 0.060 | 2/20 (H4, Panc 03.27) | inconsistent across doses |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | 0.618× | -3.2 | 0.12 | 4/22 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | 0.616× | -3.1 | 0.14 | 6/20 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.633× | -3.1 | 0.15 | 2/19 (H4, hTERT-HPNE) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.636× | -3.0 | 0.15 | 12/18 (SNU-423, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 31.2 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 11.1× (z +12.8) | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.140× (z -10.4) |
| [[A-172 (line)]] | wt | 9.56 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0501× (z -10.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.0806× (z -9.5) |
| [[SNU-423 (line)]] | alt | 9.24 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.0505× (z -11.1) |
| [[A498 (line)]] | wt | 3.98 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 2.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 0.833 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.3× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 3.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 5.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 0.958 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 1.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +8.8) | — |
| [[A-427 (line)]] | wt | 0.136 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.254 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.551 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.542 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.689 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.172 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.772 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.172 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.178 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI16]] | +0.80 | +0.75 / +0.77 | both halves | 7e-06 | STRING 465 |
| [[SAMD9L]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 | STRING 718 |
| [[XAF1]] | +0.77 | +0.70 / +0.77 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 517 |
| [[DHX58]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | STRING 408 |
| [[SAMD9]] | +0.76 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[DDX60]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | STRING 451 |
| [[EPSTI1]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 | STRING 698 |
| [[GBP4]] | +0.75 | +0.62 / +0.80 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 853 |
| [[OASL]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 556 |
| [[IFIH1]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 621 |
| [[DDX60L]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[GBP1]] | +0.74 | +0.64 / +0.78 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 908 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 6, C 12. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OASL]] | B | OASL activity raises GBP5's level | lines that do not express OASL (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without OASL | 0.035 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[IL32]] | B | IL32 activity raises GBP5's level | lines that do not express IL32 (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without IL32 | 0.067 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[IFIT3]] | B | IFIT3 activity raises GBP5's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without IFIT3 | 0.085 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[GBP3]] | B | GBP3 activity raises GBP5's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without GBP3 | 0.086 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[IFI44]] | B | IFI44 activity raises GBP5's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without IFI44 | 0.093 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[JAK2]] | B | JAK2 activity raises GBP5's level | compounds that target JAK2: 2 of 3 lower it (Fedratinib, Tofacitinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |
| [[ABI3BP]] | C | ABI3BP activity raises GBP5's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.69× lower at baseline in the lines without ABI3BP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[LMO2]] | C | LMO2 activity raises GBP5's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without LMO2 | 0.031 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent; co-absent with the target |
| [[IFI16]] | C | IFI16 activity raises GBP5's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without IFI16 | 0.039 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF; co-absent with the target |
| [[TNFAIP6]] | C | TNFAIP6 activity raises GBP5's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.35× lower at baseline in the lines without TNFAIP6 | 0.044 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[GBP2]] | C | GBP2 activity raises GBP5's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.00× lower at baseline in the lines without GBP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1; co-absent with the target |
| [[CD274]] | C | CD274 activity raises GBP5's level | lines that do not express CD274 (18) vs lines expressing it (32) | 1.98× lower at baseline in the lines without CD274 | 0.048 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2; co-absent with the target |

### Downstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 28, C 28. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IKBKE]] | B | GBP5 activity raises IKBKE's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without GBP5 | 8e-04 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[NEURL3]] | B | GBP5 activity raises NEURL3's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.07× lower at baseline in the lines without GBP5 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[SP100]] | B | GBP5 activity raises SP100's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without GBP5 | 0.010 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[PML]] | B | GBP5 activity raises PML's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without GBP5 | 0.016 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[UBE2L6]] | B | GBP5 activity raises UBE2L6's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.56× lower at baseline in the lines without GBP5 | 0.017 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[GBP3]] | B | GBP5 activity raises GBP3's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.14× lower at baseline in the lines without GBP5 | 0.022 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[MOB3C]] | B | GBP5 activity raises MOB3C's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.38× lower at baseline in the lines without GBP5 | 0.024 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[RBM43]] | B | GBP5 activity raises RBM43's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without GBP5 | 0.025 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[IFIT3]] | B | GBP5 activity raises IFIT3's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.89× lower at baseline in the lines without GBP5 | 0.026 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[SAMD9]] | B | GBP5 activity raises SAMD9's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without GBP5 | 0.027 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[KIAA1217]] | B | GBP5 activity raises KIAA1217's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without GBP5 | 0.030 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[IFIT2]] | B | GBP5 activity raises IFIT2's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.74× lower at baseline in the lines without GBP5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.3, 52.3); signed map (63.0, 30.8). **Vector** length 60.4, 16.3% of its response variance represented; |z| ≥ 3 in 666 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.61 to 56); *interferon gamma response* (hallmark, mean cos +0.62 to 60); *interferon* (control, mean cos +0.69 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +21.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +14.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +8.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +3.0 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.0 | -1.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | guanylate binding protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:89,256,189-89,272,860 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Guanylate binding proteins |
| Reactome | 5 pathways, smallest: GBP-mediated host defense; Interferon gamma signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PP8](https://www.uniprot.org/uniprotkb/Q96PP8) (Guanylate-binding protein 5):

> Interferon (IFN)-inducible GTPase that plays important roles in innate immunity against a diverse range of bacterial, viral and protozoan pathogens (By similarity). Hydrolyzes GTP, but in contrast to other family members, does not produce GMP. Following infection, recruited to the pathogen-containing vacuoles or vacuole-escaped bacteria and acts as a positive regulator of inflammasome assembly by promoting the release of inflammasome ligands from bacteria (By similarity). Acts by promoting …

**Summary**, from NCBI Gene [115362](https://www.ncbi.nlm.nih.gov/gene/115362):

> This gene belongs to the TRAFAC class dynamin-like GTPase superfamily. The encoded protein acts as an activator of NLRP3 inflammasome assembly and has a role in innate immunity and inflammation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:19895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19895) · Entrez [115362](https://www.ncbi.nlm.nih.gov/gene/115362) · UniProt [Q96PP8](https://www.uniprot.org/uniprotkb/Q96PP8) · Ensembl [ENSG00000154451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154451)

## Data

Gene col 7807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7807); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7807]; `tensor/DDL_lfc|DDL_z.npy` [7807]; `embed/gene_vectors.npy` [7807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7807 or target_col == 7807). Every well: [[GBP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
