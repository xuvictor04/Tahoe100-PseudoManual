---
symbol: "CCDC28A"
type: "gene"
col: 358
ensembl_id: "ENSG00000024862"
name: "coiled-coil domain containing 28A"
location: "6q24.1"
module: 76
arm: "+"
pooled_cpm: 25.72
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 31
n_dd_up_clean: 9
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# CCDC28A

*coiled-coil domain containing 28A* — 6q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.34× (z +14.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.162× (z -27.9, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.186× (z -15.2, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AUH]] (+0.80, fdr 7e-06), [[CRIPT]] (+0.76, fdr 7e-06), [[KLHDC3]] (+0.74, fdr 7e-06); moves opposite to [[DHX37]] (-0.63, fdr 1e-05), [[PPRC1]] (-0.60, fdr 7e-06), [[DNAJC11]] (-0.60, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +14.7 | 0e+00 | 45/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +14.0 | 2e-42 | 46/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +12.9 | 1e-35 | 45/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +4.7 | 3e-04 | 17/48 (PANC-1, A-172, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 0.001 | 18/47 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.004 | 16/48 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.17× | +3.9 | 0.008 | 17/48 (J82, A498, …) | two highest doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.008 | 12/47 (A-427, AsPC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.036 | 9/47 (AsPC-1, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[IQ 1 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.068 | 6/45 (SW480, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.068 | 5/48 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.084 | 11/48 (HT-29, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.162×** | -27.9 | 0e+00 | 48/48 (KATO III, HT-29, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.186×** | -15.2 | 0e+00 | 44/47 (SW1417, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.194×** | -14.8 | 0e+00 | 44/47 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.405×** | -14.8 | 0e+00 | 44/48 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.218×** | -13.8 | 2e-41 | 44/47 (HT-29, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.223×** | -13.6 | 3e-40 | 45/48 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.245×** | -12.8 | 2e-35 | 42/48 (KATO III, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.607×** | -12.1 | 1e-31 | 35/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.399×** | -11.4 | 3e-28 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.550×** | -10.0 | 1e-21 | 36/48 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.491×** | -8.8 | 7e-17 | 40/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.505×** | -8.5 | 1e-15 | 38/48 (SNU-423, NCI-H1792, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.426×** | -7.7 | 5e-13 | 32/45 (HepG2/C3A, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.640×** | -7.3 | 1e-11 | 32/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.488×** | -6.5 | 3e-09 | 23/48 (SW480, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -6.4 | 6e-09 | 23/48 (PANC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.3 | 2 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -17.9) |
| [[HT-29 (line)]] | alt | 35.9 | 1 | 6 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.97× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0691× (z -19.6) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0843× (z -10.8) |
| [[SW480 (line)]] | alt | 36.1 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.68× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.123× (z -17.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.368× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 0 | 6 (1 ⚠) | — | [[TAK-733 (drug)]] 5 µM 0.0254× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.163× (z -12.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.0) |
| [[KATO III (line)]] | alt | 45.6 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.33× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0603× (z -20.5) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0772× (z -11.1) |
| [[LoVo (line)]] | wt | 13.9 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +9.0) | [[TAK-733 (drug)]] 5 µM 0.0537× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 26.5 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.60× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.165× (z -14.8) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.135× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 26.4 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0579× (z -17.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.200× (z -15.3) |
| [[Hs 766T (line)]] | wt | 23.0 | 0 | 3 (1 ⚠) | — | [[EX229 (drug)]] 0.05 µM 0.119× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 35.2 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.121× (z -13.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0823× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 15.8 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.173× (z -12.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.127× (z -11.7) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.183× (z -10.5) |
| [[SW1417 (line)]] | alt | 32.8 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0808× (z -16.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0537× (z -11.4) |
| [[A-427 (line)]] | wt | 29.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -18.8) |
| [[H4 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -9.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[IQ 1 (drug)]] 0.5 µM 0.0592× (z -9.2) |
| [[HCT15 (line)]] | alt | 36.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.139× (z -10.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0552× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.133× (z -13.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0642× (z -10.6) |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -13.2) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.249× (z -9.0) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 50.4 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.126× (z -15.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.7) |
| [[A498 (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.152× (z -11.6) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -11.8) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.147× (z -9.8) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.114× (z -10.9) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.133× (z -9.7) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -10.8) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.143× (z -11.0) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 30.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0952× (z -15.2) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -9.2) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.164× (z -11.4) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.132× (z -11.3) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -10.0) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.190× (z -9.8) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.115× (z -9.0) |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.201× (z -8.8) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AUH]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[CRIPT]] | +0.76 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[KLHDC3]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[MARF1]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[MKRN1]] | +0.73 | +0.74 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[MED30]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.72 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.72 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[CALCOCO1]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[YPEL2]] | +0.71 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[SERINC1]] | +0.70 | +0.62 / +0.81 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.70 | +0.60 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX37]] | -0.63 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[PPRC1]] | -0.60 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[SNHG26]] | -0.59 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[CYREN]] | -0.59 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[PUS1]] | -0.58 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[PRORP]] | -0.58 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[GTPBP4]] | -0.57 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[P2RY11]] | -0.56 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[NOP56]] | -0.56 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[UTP20]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[NOP2]] | -0.56 | -0.61 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CCDC28A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.877). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.5, -45.5); signed map (-18.9, 9.9). **Vector** length 134, 39.6% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.0 | +14.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.2 | +12.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.2 | +14.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.4 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | +3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Alpelisib (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.3 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -18.7 | -27.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.6 | -14.8 |
|  | [[EX229 (drug)]] 5 µM |  | -11.4 | -15.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.7 | -12.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -10.4 | -13.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -9.9 | -13.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 28A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.1 — chr6:138,773,769-138,793,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CCRL1AP, DKFZp586D0623, LTAP2A; previously C6orf80 |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

UniProt [Q8IWP9](https://www.uniprot.org/uniprotkb/Q8IWP9) carries no function annotation.

**Summary**, from NCBI Gene [25901](https://www.ncbi.nlm.nih.gov/gene/25901):

> This gene encodes a coiled-coil domain containing protein. Although the specific function of this gene has not yet been determined, this gene is a known translocation partner of nucleoporin 98 in acute leukemias. The resulting fusion gene produces a nucleoporin 98-coiled-coil domain-containing protein 28A chimeric protein which may be involved in promoting myeloproliferative neoplasms. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:21098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21098) · Entrez [25901](https://www.ncbi.nlm.nih.gov/gene/25901) · UniProt [Q8IWP9](https://www.uniprot.org/uniprotkb/Q8IWP9) · Ensembl [ENSG00000024862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000024862)

## Data

Gene col 358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 358); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 358]; `tensor/DDL_lfc|DDL_z.npy` [358]; `embed/gene_vectors.npy` [358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 358 or target_col == 358). Every well: [[CCDC28A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC28A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
